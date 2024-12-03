from typing import List, Set
from .error import Error, FatalError
from .filemanager import FileManager
from collections import Counter


class Database(FileManager):
    def __init__(self, database_name):
        super().__init__(database_name)
        self._database_name = database_name
        self.__schemas: List[dict] = []
        self.__data: dict = {}

    def define_schema(self, schemas: List[dict]) -> 'Database':
        if not schemas:
            raise FatalError(
                "Schema is required while calling 'define_schema' method, but got none")

        if isinstance(schemas, dict):
            self.__create_schema(schemas)

        elif isinstance(schemas, list):
            for schema in schemas:
                if isinstance(schema, dict):
                    self.__create_schema(schema)
                else:
                    raise FatalError(
                        "Invalid schema provided.")
        else:
            raise FatalError(
                "Invalid schema provided.")
        print(self.__data)
        return self

    def insert(self, collection, data: dict) -> None:
        collection = collection.lower()
        if not self.__is_collection_available(collection):
            raise Error(
                f"Database '{self.database}' has no collection named {collection}.")
        pass
        if not data:
            raise Error(f"No data provided to the insert method")

        collection_schema = self.__get_schema_by_name(collection)
        if not isinstance(collection_schema, dict):
            raise Error(
                f"Failed to insert data due to collection schema error.")
        if Counter(data.keys()) != Counter([field["name"] for field in self.__get_schema_by_name(collection)["fields"]]):
            raise Error(f"Failed to insert data due to missing data.")

        if self.__data[collection]:
            if isinstance(self.__data[collection], list):
                self.__data[collection].append(data)
        else:
            self.__data[collection] = [data]
        self._write_collection_data(collection, [data])

    def __get_schema_by_name(self, collection: str) -> dict:
        collection = collection.lower()
        for schema in self.__schemas:
            if schema["name"] == collection:
                return schema
        return None

    def __is_collection_available(self, collection: str) -> bool:
        if not isinstance(collection, str):
            raise FatalError(f"Collection's name can only be of type string, but got {
                             type(collection)} instead.")
        return len([schema for schema in self.__schemas if schema["name"] == collection]) == 1

    def __create_schema(self, schema: dict) -> None:
        validated_schema = self.__validate_schema(schema)
        self.__schemas.append(validated_schema)
        self._create_database_files(self.__schemas)
        collected_collection = self.__data.keys()
        if not schema["name"].lower() in collected_collection:
            self.__data[schema["name"].lower()
                        ] = self._get_collection_file_data(schema)


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
            try:
                raise Error(f"Invalid attributes '{
                    ", ".join(invalid_attributes)}' provided in schema. Libz will create schema by ignoring them.")
            except Error as e:
                e.handle()

        if not isinstance(schema["name"], str) or not schema["name"].isalpha():
            raise FatalError(
                "Schema's 'name' attribute must only be of alphabets.")

        if not isinstance(schema["fields"], list):
            raise FatalError(
                "For defining a schema, attribiute 'field' must of a list..")

        validated_schema: dict = {}
        validated_schema["name"] = schema["name"].lower()
        if len([schema for schema in self.__schemas if schema["name"] == validated_schema["name"]]) != 0:
            raise FatalError(
                f"'{validated_schema["name"]}' schema is redefined.")
        validated_schema["fields"] = self.__validate_schema_field(
            validated_schema["name"], schema["fields"])
        return validated_schema

    def __validate_schema_field(self, schema_name: str,  fields: List) -> List:
        primary: str = None
        validated_fields_name: List[str] = []
        validated_fields: List[dict] = []

        for field in fields:
            valid_types = ["text", "number", "boolean", "date"]
            current_field: dict = {}
            if not isinstance(field, dict):
                raise FatalError(f"Invalid datatype for fields in '{
                                 schema_name}' schema. ")

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

            if not isinstance(field["name"], str) or not field["name"].isalpha():
                raise FatalError(
                    "Field's 'name' attribute for schema must only be of alphabets.")

            if field["name"] in validated_fields_name:
                raise FatalError(f" Duplicate name for the field provided. Got '{
                                 field["name"]}' as field name for multiple time.")

            current_field["name"] = f"{
                field["name"].strip().replace(" ", "_")}"

            if field["type"] not in valid_types:
                raise FatalError(
                    f"Inavlid data type for 'type' attributes. Valid types are {valid_types}.")
            current_field["type"] = field["type"]

            if "unique" in field_attributes:
                if not isinstance(field["unique"], bool):
                    raise FatalError(
                        f"Invalid data type for 'unique' attributes- only boolean values are acceptable.")
                current_field["unique"] = field["unique"]
            else:
                current_field["unique"] = False

            if "primary" in field_attributes:
                if not isinstance(field["primary"], bool):
                    raise FatalError(
                        f"Invalid data type for 'primary' attributes- only boolean values are acceptable.")

                if primary is not None:
                    raise FatalError(
                        f"Only one field can be made primary. '{primary}' is already defined as primary but '{
                            field["name"]}' is again defined as primary"
                    )
                primary = field["primary"]
            else:
                primary = True if primary is None else False

            current_field["primary"] = primary
            validated_fields.append(current_field)
        return validated_fields
