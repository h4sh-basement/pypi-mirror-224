from .vendor.errors import AvdValidationError


class ValidationResult:
    """
    Object containing result of data validation

    Attributes:
        failed: True if data is not valid according to the schema. Otherwise False.
        validation_errors: List of AvdValidationErrors containing schema violations.
    """

    failed: bool
    validation_errors: list[AvdValidationError]

    def __init__(self, failed: bool, validation_errors: list):
        self.failed = failed
        self.validation_errors = validation_errors
