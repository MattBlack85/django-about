import datetime

from pytz import timezone

from django.core.exceptions import ValidationError


def has_valid_date(date):
    if not date >= datetime.datetime.now(tz=timezone('UTC')):
        raise ValidationError("%s happened in the past" % date)
