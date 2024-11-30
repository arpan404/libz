from error import Error, FatalError
from typing import Set, List


class Database:
    def __init__(self, database_name):
        self._database_name = database_name
        self.__schemas: Set[dict] = []

    def _define_schema(self, schemas: List[dict]) -> 'Database':
        if not schemas:
            raise FatalError(
                "Schema is required while calling 'define_schema' method, but got none")

        if isinstance(schemas, dict):
            self.__create_schema(schemas)

        if isinstance(schemas, list):
            for schema in schemas:
                if isinstance(schema, dict):
                    self.__create_schema(schema)
                else:
                    raise FatalError(
                        "Invalid schema provided.")
        else:
            raise FatalError(
                "Invalid schema provided.")

        return self

    def __create_schema(self, schema: dict) -> None:
        validated_schema = self.__validate_schema(schema)
        self.__schemas.add(validated_schema)

    def __validate_schema(self, schema: dict) -> dict:
        schema_attributes = schema.keys()
        valid_schema_attributes = ["name", "fields"]

        missing_schema_atrributes = [
            attribute for attribute in valid_schema_attributes if attribute not in schema_attributes]

        if missing_schema_atrributes:
            raise FatalError(
                f"For defining a schema, '{", ".join(missing_schema_atrributes)}' attributes are required, which were not provided.")

        invalid_attributes = [
            attribute for attribute in schema_attributes if attribute not in valid_schema_attributes]

        if invalid_attributes:
            raise Error(f"Invalid attributes '{
                        ", ".join(invalid_attributes)}' provided in schema. Libz will create schema by ignoring them.")

        if isinstance(schema.name, str) or not schema.name.isalpha():
            raise FatalError(
                "Schema's 'name' attribute must only be of alphabets.")

        if not isinstance(schema.fields, list):
            raise FatalError(
                "For defining a schema, attribiute 'field' must of a list..")

        validated_schema: dict = {}
        validated_schema["name"] = schema.name.lower()

        primary = None
        validated_fields_name = []
        for field in schema.fields:
            if isinstance(field, dict):
                raise FatalError(f"Invalid datatype for fields in '{
                                 validated_schema.name}' schema.. ")

            valid_field_attributes = ["name", "type", "unique", "primary"]
            optional_field_attributes = ["unique", "primary"]
            field_attributes = field.keys()

            required_attributes = [
                attr for attr in valid_field_attributes if attr not in optional_field_attributes]

            missing_attributes = [
                attribute for attribute in required_attributes if attribute not in field_attributes]

            if missing_attributes:
                raise FatalError(
                    f"Attributes - {", ".join(missing_attributes)} are missing in the schema.")

            if not isinstance(field.name, str) or not field.name.isalpha():
                "Field's 'name' attribute for schema must only be of alphabets."

            if field.name in validated_fields_name:
                raise FatalError(f" Duplicate name for the field provided. Got '{
                                 field.name}' as field name for multiple time.")

            