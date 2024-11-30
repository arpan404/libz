from error import Error, FatalError
from typing import Set


class Database:
    database_name: str = None
    database_schema: dict = None

    def __init__(self, database_name):
        if (Database.database_name is not None):
            raise Error(
                "Database is already initialized. Reinitialization is not allowed.")
        Database.database_name = database_name

    def defineSchema(self, schema):
        """
        example:
        Database.defineSchema(
            {
                name: "users",
                fields:[
                    "uid": {
                        type: "text",
                        unique: True,
                        primary: True
                    },
                    "firstName":{
                        type:"text",
                        unique: False
                    },
                    "joinedDate":{
                        type:"date"
                    }
                ]
            }
        )
        """

        validTypes: Set[str] = {"text", "number", "boolean", "date"}

        if (not schema.name):
            raise FatalError(
                "Name for the schema is required, but was not provided.")

        if (not isinstance(schema.name, str)):
            raise FatalError(f"Name for the scheme should always be string, but instead got '{type(schema.name)}'")

        if not schema.fields:
            raise FatalError(f"Fields for the '{schema.name}' not provided")

        for field in schema.fields:
            # if not filed.type
            pass
