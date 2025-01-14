from typing import Generator

from .validation_result import ValidationResult
from .vendor.errors import AvdConversionWarning, AvdDeprecationWarning, AvdValidationError
from .vendor.schema.avdschema import AvdSchema

IGNORE_EXCEPTIONS = (AvdDeprecationWarning, AvdConversionWarning)
RETURN_EXCEPTIONS = AvdValidationError


class AvdSchemaTools:
    """
    Tools that wrap the various schema components for easy use
    """

    def __init__(self, schema: dict = None, schema_id: str = None) -> None:
        """
        Convert data according to the schema (convert_types)
        The data conversion is done in-place (updating the original "data" dict).

        Args:
            schema_id:
                Name of AVD Schema to use for conversion and validation.
        """
        self.avdschema = AvdSchema(schema=schema, schema_id=schema_id)

    def convert_data(self, data: dict) -> None:
        """
        Convert data according to the schema (convert_types)
        The data conversion is done in-place (updating the original "data" dict).

        Args:
            data:
                Input variables which should be converted according to the schema.
        """

        # avdschema.convert returns a Generator, so we have to iterate through it to perform the actual conversions.
        exceptions: Generator = self.avdschema.convert(data)
        for exception in exceptions:
            # Ignore conversions and deprecations
            if isinstance(exception, IGNORE_EXCEPTIONS):
                continue

            if isinstance(exception, Exception):
                raise exception

        return None

    def validate_data(self, data: dict) -> ValidationResult:
        """
        Validate data according to the schema

        Args:
            data:
                Input variables which are to be validated according to the schema.

        Returns:
            Instance of ValidationResult, where "failed" is True if data is invalid and "errors" is a list of AvdValidationError.
        """
        result = ValidationResult(failed=False, validation_errors=[])

        # avdschema.validate returns a Generator, so we have to iterate through it to perform the actual validations.
        exceptions: Generator = self.avdschema.validate(data)
        for exception in exceptions:
            # Ignore conversions and deprecations
            if isinstance(exception, IGNORE_EXCEPTIONS):
                continue

            if isinstance(exception, RETURN_EXCEPTIONS):
                result.validation_errors.append(exception)
                result.failed = True
                continue

            if isinstance(exception, Exception):
                raise exception

        return result

    def convert_and_validate_data(self, data: dict) -> dict:
        """
        Convert and validate data according to the schema

        Returns dictionary to be compatible with Ansible plugin. Called from vendored "get_structured_config".

        Args:
            data:
                Input variables which are to be validated according to the schema.

        Returns
            dict :
                failed : bool
                    True if data is invalid. Otherwise False.
                errors : list[Exception]
                    Any data validation issues.
        """
        self.convert_data(data)
        res = self.validate_data(data)
        return {"failed": res.failed, "errors": res.validation_errors}
