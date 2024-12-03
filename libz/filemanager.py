from typing import List
from .error import FatalError
import os


class FileManager:
    def __init__(self, database_name: str):
        self.database = database_name

    def _create_database_files(self, database_schemas):
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

        database_main_file_text = ""
        for schema in database_schemas:
            database_main_file_text += f"\n\n{schema['name']}\n"
            for field in schema["fields"]:
                database_main_file_text += f"{field['name']}\t{
                    field['type']}\t{field['unique']}\t{field['primary']}\n"
            directory_path = os.path.join(
                database_directory, f"{self.database}_{schema['name']}_collection.txt")
            if not self.__does_path_exists(directory_path):
                self.__create_files(directory_path, "")
        self.__create_files(database_main_file_path,
                            database_main_file_text)

    def _write_collection_data(self, collection_name, collection_data: List[dict]) -> None:
        if not isinstance(collection_data, list):
            raise FatalError(
                f"Writing data to disk failed. Expectd list but got {type(collection_data)}")
        text_to_write = ""
        for data in collection_data:
            if not isinstance(data, dict):
                raise FatalError(
                    f"Writing data to the disk due to invalid datatype passed.")
            text_to_write += self.__prepare_collection_data(data)+"\n"

        try:
            collection_file_path = os.path.join(
                os.getcwd(), self.database, f"{self.database}_{collection_name}_collection.txt")
            with open(collection_file_path, "a") as file:
                file.write(text_to_write)
        except:
            raise FatalError("Failed to write data to the disk.")

    def _get_collection_file_data(self, collection: dict) -> List[dict]:
        if not isinstance(collection, dict):
            raise FatalError("Invalid data type for collection.")
        collection_data = []
        try:
            collection_file_path = os.path.join(
                os.getcwd(), self.database, f"{self.database}_{collection["name"]}_collection.txt")
            with open(collection_file_path, "r") as file:
                collection_file_data = file.readlines()
        except:
            raise FatalError("Failed to open collection file.")

        for line in collection_file_data:
            new_line = line.strip()
            collection_data.append(self.__prepare_collected_data(
                collection["fields"], new_line))
        return collection_data

    def __prepare_collected_data(self, fields: List[dict], collected_data: str) -> dict:
        data_dict = {}
        data_values = collected_data.split(',\t')

        for index, field in enumerate(fields):
            if index < len(data_values):
                field_name = field['name']
                data_dict[field_name] = data_values[index].strip("'").strip('"')
        return data_dict

    def __prepare_collection_data(self, collection_data: dict) -> str:
        prepared_string = ""
        for data in collection_data.values():
            prepared_string += f"{repr(data)},\t"
        return prepared_string

    def __create_files(self, file_path: str, text: str) -> None:
        try:
            with open(file_path, "w") as f:
                f.write(text)
        except:
            raise FatalError(
                f"Something went wrong. Could not create a database file at {file_path}.")

    def __does_path_exists(self, path: str) -> bool:
        return os.path.exists(path)
