from .error import FatalError
import os


class FileManager:
    def __init__(self, database_name: str):
        self.database = database_name

    def _create_database_files(self):
        current_directory = os.getcwd()
        database_directory = os.path.join(current_directory, self.database)
        try:
            if self.__does_path_exists(database_directory):
                os.mkdir(database_directory)
        except:
            raise FatalError(
                "Something went wrong. Could not create a database directory.")
        

    def __is_file_empty(fsel, filePath: str) -> bool:
        return True if os.stat(filePath).st_size == 0 else False

    def __does_path_exists(self, path: str) -> bool:
        return os.path.exists(path)
