from datetime import datetime

from django.core.exceptions import ValidationError


def check_date_not_past(value: datetime):
    print(datetime.today())
    if value < datetime.today():
        raise ValidationError(f"{value} is in the past.")