from abc import ABC, abstractmethod
import json
from AIBridge.exceptions import AIBridgeException, ValidationException
import csv
import io
import xml.etree.ElementTree as ET
import re
import sqlparse
from json import JSONDecodeError
import jsonschema


class Validation(ABC):
    @abstractmethod
    def validate(self, output_string, schema):
        pass


class JsonSchema(Validation):
    def validate(self, output_string, schema=None):
        try:
            json_data = json.loads(output_string)
        except AIBridgeException as e:
            raise JSONDecodeError(f" Error in the AI output for the validation->{e}")
        if schema:
            try:
                user_schema = json.loads(schema)
            except AIBridgeException as e:
                raise JSONDecodeError(f"Error in the schema you entred {e}")
            try:
                jsonschema.Draft7Validator.check_schema(user_schema)
                jsonschema.Draft7Validator.check_schema(json_data)
            except jsonschema.exceptions.SchemaError as e:
                raise ValidationException(f"Invalid output JSON schema: {e}")
        return json.dumps(json_data)


class CSVSchema(Validation):
    def validate(self, output_string, schema=None):
        try:
            csv_data = output_string.strip().split("\n")
            header_row = csv_data[0] if csv_data else None

            def validate_csv(header_row, schema):
                if not header_row:
                    return False
                if "," not in header_row:
                    return False
                if schema:
                    header_columns = [
                        column.strip().lower() for column in header_row.split(",")
                    ]
                    expected_columns = expected_columns = [
                        column.strip().lower() for column in schema.split(",")
                    ]
                    if not expected_columns:
                        expected_columns = expected_columns = [
                            column.strip().lower() for column in schema.split("")
                        ]
                    print(header_columns, expected_columns)
                    if len(header_columns) != len(expected_columns):
                        return False
                    for key in header_columns:
                        if key not in expected_columns:
                            return False
                return True

            result = validate_csv(header_row, schema)
            if not result:
                raise ValidationException(
                    f"Csv schema genrated by AI is not a valid schema"
                )
            return output_string
        except csv.Error as e:
            raise ValidationException(f"{e}")


class SQLSchema(Validation):
    def validate(self, output_string, schema=None):
        sql_keywords = [
            "SELECT",
            "UPDATE",
            "INSERT",
            "DELETE",
            "FROM",
            "WHERE",
            "JOIN",
        ]
        pattern = r"\b(?:{})\b".format("|".join(sql_keywords))
        if re.search(pattern, output_string, re.IGNORECASE):
            parsed = sqlparse.parse(output_string)
            if any(parsed):
                return output_string
            else:
                raise ValidationException(
                    f"Sql schema genrated by AI is not a valid schema"
                )
        else:
            raise ValidationException(
                f"Sql schema genrated by AI is not a valid schema"
            )


class XMLSchema(Validation):
    def validate(self, output_string, schema=None):
        print(output_string)
        try:
            output_schema = ET.fromstring(output_string)
        except AIBridgeException as e:
            raise ValidationException(
                f"Xml schema genrated by AI is not a valid schema->{e}"
            )
        if schema:
            input_schema = ET.fromstring(schema)

            def validate_xml(output_schema, input_schema):
                if output_schema.tag != input_schema.tag:
                    return False
                if output_schema.attrib != input_schema.attrib:
                    return False
                for child1, child2 in zip(output_schema, input_schema):
                    if not validate_xml(child1, child2):
                        return False

                return True

            result = validate_xml(output_schema, input_schema)
            if not result:
                raise ValidationException(
                    f"Xml schema genrated by AI is not a valid schema"
                )
        return output_string
