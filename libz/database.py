from error import Error


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
                fields:{
                    "uid": {
                        type: "string",
                        unique: True,
                        primary: True
                    },
                    "firstName":{
                        type:"string",
                        unique: False
                    },
                    "joinedDate":{
                        type:"date"
                    }
                }
            }
        )
        """
        
        
