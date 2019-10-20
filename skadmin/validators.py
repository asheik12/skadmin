from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone(value):
    if not value.isdigit():
        raise ValidationError(_('Only number are allowed'),)
    elif len(value) < 10:
        raise ValidationError(_('Invalid mobile, requires 10 digits'),)
    