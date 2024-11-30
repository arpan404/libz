from .error import Error, FatalError
from typing import List, Set
from .database import Database


class Libz(Database):
    libz_databases: Set[str] = set()

    def __init__(self, database_name):
        if Libz.libz_databases and database_name in Libz.libz_databases:
            raise FatalError(
                "Same database is reinitialized, which is not allowed."
            )
        super().__init__(database_name)
        Libz.libz_databases.add(database_name)
        self.database_schema: List[dict] = []
