from django.core.exceptions import ValidationError

def validate_password(value):
    if len(value) < 6:
        raise ValidationError('Пароль должень состоять минимум из 6 символов')

    if not any(char.isupper() for char in value):
        raise ValidationError('Пароль должен содержать как миниму 1 заглавную букву')

    if not any(char.isdigit() for char in value):
        raise ValidationError('Пароль должен содержать как миниму 1 цифру')