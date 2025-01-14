from collections import defaultdict
from logging import getLogger
from typing import Dict, List

from NEMO.decorators import accounting_or_user_office_or_manager_required
from NEMO.models import Account, AdjustmentRequest, Project, User
from NEMO.utilities import BasicDisplayTable, export_format_datetime, format_datetime
from NEMO.views.customization import UserRequestsCustomization
from NEMO.views.usage import date_parameters_dictionary, get_managed_projects, get_project_applications
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from NEMO_billing.invoices.customization import BillingCustomization
from NEMO_billing.invoices.models import InvoiceConfiguration, InvoiceDetailItem
from NEMO_billing.invoices.processors import BillableItem, invoice_data_processor_class as data_processor
from NEMO_billing.invoices.utilities import display_amount
from NEMO_billing.templatetags.billing_tags import cap_discount_installed

logger = getLogger(__name__)


@login_required
@require_GET
def usage(request):
    user: User = request.user
    user_managed_projects = get_managed_projects(user)
    base_dictionary, start, end, kind, identifier = date_parameters_dictionary(request)
    customer_filter = Q(customer=user) | Q(project__in=user_managed_projects)
    user_filter = Q(user=user) | Q(project__in=user_managed_projects)
    trainee_filter = Q(trainee=user) | Q(project__in=user_managed_projects)
    project_id = request.GET.get("project") or request.GET.get("pi_project")
    csv_export = bool(request.GET.get("csv", False))
    if user_managed_projects:
        base_dictionary["selected_project"] = "all"
    if project_id:
        project = get_object_or_404(Project, id=project_id)
        if request.GET.get("project"):
            base_dictionary["selected_user_project"] = project
        else:
            base_dictionary["selected_project"] = project
        customer_filter = customer_filter & Q(project=project)
        user_filter = user_filter & Q(project=project)
        trainee_filter = trainee_filter & Q(project=project)
    config = InvoiceConfiguration.first_or_default()
    detailed_items = sorted_billable_items(start, end, config, customer_filter, user_filter, trainee_filter)
    if csv_export:
        return csv_export_response(detailed_items)
    else:
        total_charges = sum(item.billable_amount for item in detailed_items)
        dictionary = {
            "detailed_items": detailed_items,
            "total_charges": display_amount(total_charges, config),
            "can_export": True,
            "adjustment_time_limit": UserRequestsCustomization.get_date_limit(),
            "existing_adjustments": get_existing_adjustments(user),
        }
        if BillingCustomization.get_bool("billing_usage_show_pending_vs_final"):
            dictionary["pending_charges"] = display_amount(
                total_charges - sum(item.invoiced_amount or 0 for item in detailed_items), config
            )
        if user_managed_projects:
            dictionary["pi_projects"] = user_managed_projects
        dictionary["no_charges"] = not dictionary["detailed_items"]
        if cap_discount_installed():
            from NEMO_billing.cap_discount.models import CAPDiscount

            if CAPDiscount.objects.filter(user=user).exists():
                dictionary["cap_discounts_url"] = reverse("usage_cap_discounts")
        if user_managed_projects and any(
            [getattr(project, "projectprepaymentdetail", None) for project in user_managed_projects if project.active]
        ):
            dictionary["project_prepayments_url"] = reverse("usage_project_prepayments")

        return render(request, "invoices/usage.html", {**base_dictionary, **dictionary})


@accounting_or_user_office_or_manager_required
@require_GET
def project_usage(request):
    base_dictionary, start, end, kind, identifier = date_parameters_dictionary(request)

    detailed_items: List[BillableItem] = []
    config = InvoiceConfiguration.first_or_default()

    projects = []
    user = None
    account = None
    selection = ""
    try:
        if kind == "application":
            projects = Project.objects.filter(application_identifier=identifier)
            selection = identifier
        elif kind == "project":
            projects = [Project.objects.get(id=identifier)]
            selection = projects[0].name
        elif kind == "account":
            account = Account.objects.get(id=identifier)
            projects = Project.objects.filter(account=account)
            selection = account.name
        elif kind == "user":
            user = User.objects.get(id=identifier)
            projects = user.active_projects()
            selection = str(user)

        if projects:
            customer_filter = Q(project__in=projects)
            user_filter = Q(project__in=projects)
            trainee_filter = Q(project__in=projects)
            if user:
                customer_filter = customer_filter & Q(customer=user)
                user_filter = user_filter & Q(user=user)
                trainee_filter = trainee_filter & Q(trainee=user)
            detailed_items = sorted_billable_items(start, end, config, customer_filter, user_filter, trainee_filter)
            if bool(request.GET.get("csv", False)):
                return csv_export_response(detailed_items)
    except Exception as e:
        logger.exception(e)
    total_charges = sum(item.billable_amount for item in detailed_items)
    dictionary = {
        "search_items": set(Account.objects.all())
        | set(Project.objects.all())
        | set(get_project_applications())
        | set(User.objects.filter(is_active=True)),
        "detailed_items": detailed_items,
        "total_charges": display_amount(total_charges, config),
        "pending_charges": display_amount(
            total_charges - sum(item.invoiced_amount or 0 for item in detailed_items), config
        ),
        "project_autocomplete": True,
        "adjustment_time_limit": UserRequestsCustomization.get_date_limit(),
        "existing_adjustments": get_existing_adjustments(request.user),
        "selection": selection,
        "can_export": True,
    }
    dictionary["no_charges"] = not dictionary["detailed_items"]
    if cap_discount_installed():
        from NEMO_billing.cap_discount.models import CAPDiscount

        if user and CAPDiscount.objects.filter(user=user).exists():
            dictionary["cap_discounts_url"] = reverse("usage_cap_discounts_user", args=[identifier])
        if account and CAPDiscount.objects.filter(account=account).exists():
            dictionary["cap_discounts_url"] = reverse("usage_cap_discounts_account", args=[identifier])
    return render(request, "invoices/usage.html", {**base_dictionary, **dictionary})


def sorted_billable_items(start, end, config, customer_filter, user_filter, trainee_filter) -> List[BillableItem]:
    items = data_processor.get_billable_items(start, end, config, customer_filter, user_filter, trainee_filter, False)
    augment_with_invoice_items(items)
    items.sort(key=lambda x: (-x.item_type.value, x.start), reverse=True)
    return items


def augment_with_invoice_items(billables: List[BillableItem]):
    pending_vs_final = BillingCustomization.get_bool("billing_usage_show_pending_vs_final")
    for billable in billables:
        invoice_item: InvoiceDetailItem = (
            InvoiceDetailItem.objects.filter(
                content_type__model=billable.item._meta.model_name,
                object_id=billable.item.id,
                invoice__voided_date__isnull=True,
            )
            .only("invoice", "rate", "amount", "discount")
            .first()
        )
        billable.invoiced_display_amount = invoice_item.amount_display() if invoice_item else None
        billable.invoiced_amount = invoice_item.amount if invoice_item else None
        billable.invoiced_discount = invoice_item.discount if invoice_item else None
        billable.invoiced_rate = invoice_item.rate if invoice_item else None
        billable.amount = billable.amount if not billable.invoiced_amount else None
        billable.billable_rate = billable.invoiced_rate or billable.display_rate
        billable.billable_amount = billable.invoiced_amount or billable.amount or 0
        billable.billable_display_amount = billable.invoiced_display_amount or (
            f"{'(pending) ' if pending_vs_final else ''}{billable.display_amount}" if billable.display_amount else ""
        )
        billable.merged_amount = billable.invoiced_amount or billable.amount


def csv_export_response(detailed_items: List[BillableItem]):
    table_result = BasicDisplayTable()
    table_result.add_header(("type", "Type"))
    table_result.add_header(("user", "User"))
    table_result.add_header(("username", "Username"))
    table_result.add_header(("name", "Item"))
    table_result.add_header(("project", "Project"))
    table_result.add_header(("start", "Start time"))
    table_result.add_header(("end", "End time"))
    table_result.add_header(("quantity", "Quantity"))
    table_result.add_header(("rate", "Rate"))
    table_result.add_header(("cost", "Cost"))
    pending_vs_final = BillingCustomization.get_bool("billing_usage_show_pending_vs_final")
    if pending_vs_final:
        table_result.add_header(("cost_pending", "Cost (Pending)"))
    for billable_item in detailed_items:
        billable_dict = {
            "type": billable_item.item_type.display_name(),
            "user": billable_item.user.get_name(),
            "username": billable_item.user.username,
            "name": billable_item.name,
            "project": billable_item.project.name,
            "start": format_datetime(billable_item.start, "SHORT_DATETIME_FORMAT"),
            "end": format_datetime(billable_item.end, "SHORT_DATETIME_FORMAT"),
            "quantity": billable_item.quantity,
            "rate": billable_item.invoiced_rate or (billable_item.rate.display_rate() if billable_item.rate else ""),
            "cost": round(billable_item.invoiced_amount, 2) if billable_item.invoiced_amount else "",
        }
        if pending_vs_final:
            billable_dict["cost_pending"] = round(billable_item.amount, 2) if billable_item.amount else ""
        else:
            billable_dict["cost"] = round(billable_item.merged_amount, 2) if billable_item.merged_amount else ""
        table_result.add_row(billable_dict)
    response = table_result.to_csv()
    filename = f"usage_export_{export_format_datetime()}.csv"
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


def get_existing_adjustments(user) -> Dict[int, List]:
    existing_adjustments = defaultdict(list)
    for values in (
        AdjustmentRequest.objects.filter(deleted=False, creator=user).values("item_type", "item_id").distinct()
    ):
        existing_adjustments[values["item_type"]].append(values["item_id"])
    return existing_adjustments
