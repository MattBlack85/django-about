import datetime
import factory
import random

from pytz import timezone

from factory.fuzzy import FuzzyText

from .models import MaintenanceMessage

TODAY = datetime.datetime.now(tz=timezone('UTC'))


class MaintenanceFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = MaintenanceMessage

    planned_date = factory.fuzzy.FuzzyDateTime(TODAY, TODAY + datetime.timedelta(days=10))
    reason = FuzzyText(length=random.randint(10, 25))
