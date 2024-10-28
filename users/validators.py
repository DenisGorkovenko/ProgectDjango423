import re
from django.core.exceptions import ValidationError

def validate_password(field):
    pattern = re.compile(r'[A-Za-z0-9]+$')
    if not bool(re.match(pattern, field)):
        print('Должно содержать A-Z a-z 0-9')
        raise ValidationError('Должно содержать A-Z a-z 0-9')
    if not 6 <= len(field) <= 12:
        print('Количество символов не менее 6 но не более 12')
        raise ValidationError('Количество символов не менее 6 но не более 12')