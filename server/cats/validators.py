import string
from django.core.exceptions import ValidationError


def check_cat_age(value):
    if value > 30:
        raise ValidationError('Кошка столько не проживет!')
