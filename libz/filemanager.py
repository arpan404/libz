from .error import FatalError
import os


class FileManager:
    def __init__(self, database_name: str):
        self.database = database_name

    def _create_database_files(self, database_schemas):
        print(database_schemas)
        current_directory = os.getcwd()
        database_directory = os.path.join(current_directory, self.database)
        try:
            if not self.__does_path_exists(database_directory):
                os.mkdir(database_directory)
        except:
            raise FatalError(
                "Something went wrong. Could not create a database directory.")

        database_main_file_path = os.path.join(
            database_directory, f"{self.database}_{self.database}.txt")
        if self.__is_file_empty(database_main_file_path):
            database_main_file_text = ""
            for schema in database_schemas:
                database_main_file_text += f"\n\n{schema['name']}"
                for field in schema["fields"]:
                    database_main_file_text += f"\n{field['name']}\t{
                        field['type']}\t{field['unique']}\t{field['primary']}"
                directory_path = os.path.join(
                    database_directory, f"{self.database}_{schema['name']}.txt")
                self.__create_files(directory_path, "")
            self.__create_files(database_main_file_path,
                                database_main_file_text)

    def __create_files(self, file_path: str, text: str) -> None:
        try:
            with open(file_path, "w") as f:
                f.write(text)
                pass
        except:
            raise FatalError(
                f"Something went wrong. Could not create a database file at {file_path}.")
    
    def __validate_database_file_data(self, file_path)->bool:
        try:
            # with open(file_path, )
            pass
        except:
            raise FatalError(f"Could not open the database file")
    
    def __is_file_empty(self, filePath: str) -> bool:
        try:
            return True if os.stat(filePath).st_size == 0 else False
        except:
            return True

    def __does_path_exists(self, path: str) -> bool:
        return os.path.exists(path)
