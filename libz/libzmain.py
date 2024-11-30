from error import Error, FatalError
from typing import List, Set


class Libz:
    libz_database_name: str = None

    def __init__(self, database_name):
        if Libz.libz_database_name is not None and Libz.libz_database_name == database_name:
            raise FatalError(
                "Same database is reinitialized, which is not allowed."
            )
        Libz.libz_database_name = database_name
        self.database_name = database_name
        self.database_schema: List[dict] = []

    def defineSchema(self, schema: List[dict]) -> 'Libz':
        if not schema:
            raise FatalError(
                "Schema is required while calling 'defineSchema' method, but got none")

        if isinstance(schema, dict):
            validated_schema = self.__validate_schema(schema)
            self.database_schema.append(validated_schema)

        if isinstance(schema, list):
            for individual_schema in schema:
                if isinstance(schema, dict):
                    validated_schema = self.__validate_schema(
                        individual_schema)
                    self.database_schema.append(validated_schema)
                else:
                    raise FatalError(
                        "Invalid schema provided. Check documentation for more details.")
        else:
            raise FatalError(
                "Invalid schema provided. Check documentation for more details.")

    def __validate_schema(schema: dict) -> dict:
        if not schema.name:
            raise FatalError(
                "For defining a schema, name is required, which was not provided. Check documentation for more details.")
        if not isinstance(schema.name, str):
            raise FatalError("Schema's name must only be string. Check documentation for more information.")

        if not schema.name.isalpha():
            raise FatalError("Schema's name must only be of alphabets. Check documentation for more information.")
        
        if not schema.fields:
            raise FatalError("For defining a schema, fields must be provided. Check documentation for more information.")

        if not isinstance(schema.fields, list):
            raise FatalError("For defining a schema, list of fields must be provided. Check documentation for more information.")
        
        validated_schema:dict={}
        
        validated_schema["name"] = schema.name
        
            