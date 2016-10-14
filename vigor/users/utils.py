from django.core.exceptions import ValidationError


def less_than_1000_validator(value):
    if value > 1000:
        raise ValidationError(
            "$(value) cannot be greater than 1000",
            params={"value": value}
        )
