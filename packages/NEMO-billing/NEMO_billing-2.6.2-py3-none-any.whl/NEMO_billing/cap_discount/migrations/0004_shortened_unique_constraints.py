# Generated by Django 3.2.19 on 2023-05-31 17:04
from copy import deepcopy
from typing import Dict

from django.db import DatabaseError, migrations
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


class Migration(migrations.Migration):

    dependencies = [
        ('cap_discount', '0003_multi_tier_discount'),
    ]

    operations = []

    def apply(self, project_state, schema_editor: BaseDatabaseSchemaEditor, collect_sql=False):
        # Because we changed the initial migration, we need to add/remove the constraints manually
        # We check if the old constraints exist in the DB (case when app was migrated before the change)
        # and remove them if they do. Then we add the new constraints
        current_name_of_constraint = "capdiscountconfiguration_unique_rate_category_facility"
        current_name_of_null_constraint = "capdiscountconfiguration_unique_rate_category_null_facility"
        model_state = project_state.models["cap_discount", "capdiscountconfiguration"]
        unique_constr_definition = model_state.get_constraint_by_name(current_name_of_constraint)
        unique_null_constr_definition = model_state.get_constraint_by_name(current_name_of_null_constraint)
        previous_unique_constr = deepcopy(unique_constr_definition)
        previous_unique_null_constr = deepcopy(unique_null_constr_definition)
        CapDiscountConfiguration = project_state.apps.get_model("cap_discount", "CapDiscountConfiguration")
        constraints: Dict[str, Dict] = schema_editor.connection.introspection.get_constraints(schema_editor.connection.cursor(), "cap_discount_capdiscountconfiguration")
        # Here we are just going to remove the unique constraints and re-add them
        db_previous_constr_names = []
        db_previous_null_constr_names = []
        for constraint_name, constraint in constraints.items():
            if "capdiscountconfiguration_unique_rate" in constraint_name and constraint.get("unique") == True:
                if "_null" in constraint_name:
                    db_previous_null_constr_names.append(constraint_name)
                else:
                    db_previous_constr_names.append(constraint_name)
        for db_previous_constr_name in db_previous_constr_names:
            previous_unique_constr.name = db_previous_constr_name
            try:
                schema_editor.remove_constraint(CapDiscountConfiguration, previous_unique_constr)
            except DatabaseError:
                pass
        for db_previous_null_constr_name in db_previous_null_constr_names:
            previous_unique_null_constr.name = db_previous_null_constr_name
            try:
                schema_editor.remove_constraint(CapDiscountConfiguration, previous_unique_null_constr)
            except DatabaseError:
                pass
        try:
            schema_editor.add_constraint(CapDiscountConfiguration, unique_constr_definition)
        except DatabaseError:
            pass
        try:
            schema_editor.add_constraint(CapDiscountConfiguration, unique_null_constr_definition)
        except DatabaseError:
            pass
        return project_state


def check_if_constraint_exist(connection: BaseDatabaseWrapper, table_name, constraint_name) -> bool:
    constraints: Dict[str, Dict] = connection.introspection.get_constraints(connection.cursor(), table_name)
    return constraint_name in constraints
