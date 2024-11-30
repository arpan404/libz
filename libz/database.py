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
                        "Invalid schema provided. Check documentation for more details.")
        else:
            raise FatalError(
                "Invalid schema provided. Check documentation for more details.")

        return self

    def __create_schema(self, schema: dict) -> None:
        validated_schema = self.__validate_schema(schema)
        self.__schemas.add(validated_schema)

    def __validate_schema(self, schema: dict) -> dict:
        if not schema.name:
            raise FatalError(
                "For defining a schema, name is required, which was not provided. Check documentation for more details.")
        if not isinstance(schema.name, str):
            raise FatalError(
                "Schema's name must only be string. Check documentation for more information.")

        if not schema.name.isalpha():
            raise FatalError(
                "Schema's name must only be of alphabets. Check documentation for more information.")

        if not schema.fields:
            raise FatalError(
                "For defining a schema, fields must be provided. Check documentation for more information.")

        if not isinstance(schema.fields, list):
            raise FatalError(
                "For defining a schema, list of fields must be provided. Check documentation for more information.")

        validated_schema: dict = {}

        validated_schema["name"] = schema.name
