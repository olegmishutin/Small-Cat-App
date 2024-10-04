import string
from django.core.exceptions import ValidationError


def check_cat_age(value):
    if value > 30:
        raise ValidationError('Кошка столько не проживет!')


def check_hair_color_is_hex(value):
    return any(char in string.hexdigits for char in value)
