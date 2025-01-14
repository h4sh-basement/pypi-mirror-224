from cloudquery.sdk.scalar import Scalar, ScalarInvalidTypeError, NULL_VALUE
from typing import Any


def parse_string_to_bool(input_string):
    true_strings = ["true", "t", "yes", "y", "1"]
    false_strings = ["false", "f", "no", "n", "0"]

    lower_input = input_string.lower()

    if lower_input in true_strings:
        return True
    elif lower_input in false_strings:
        return False
    else:
        raise ScalarInvalidTypeError("Invalid boolean string: {}".format(input_string))


class Bool(Scalar):
    def __eq__(self, scalar: Scalar) -> bool:
        if scalar is None:
            return False
        if type(scalar) == Bool:
            return self._value == scalar._value and self._valid == scalar._valid
        return False

    @property
    def value(self):
        return self._value

    def set(self, value: Any):
        if value is None:
            self._valid = False
            return

        if isinstance(value, Bool):
            self._valid = value.is_valid
            self._value = value.value
            return

        if type(value) == bool:
            self._value = value
        elif type(value) == str:
            self._value = parse_string_to_bool(value)
        else:
            raise ScalarInvalidTypeError(
                "Invalid type {} for Bool scalar".format(type(value))
            )

        self._valid = True
