import json

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from datetime import datetime, timedelta
from pytz import timezone

from .factories import MaintenanceFactory
from .models import MaintenanceMessage


class MaintenanceBaseTest(TestCase):

    def setUp(self):
        self.maintenance = MaintenanceFactory()

    def test_set_maintenance(self):
        self.assertEqual(1, MaintenanceMessage.objects.count())

    def test_set_maintenance_fail(self):
        m = MaintenanceMessage(
            planned_date=datetime.now(tz=timezone('UTC')) - timedelta(days=1),
            reason='some reason'
        )

        with self.assertRaises(ValidationError):
            m.full_clean()

    def test_check_no_maintenance(self):
        MaintenanceMessage.objects.all().delete()

        client = Client()
        url = reverse('about')
        response = client.get(url)
        json_response = json.loads(response.content)

        self.assertIsNone(json_response['maintenance'])

    def test_check_maintenance(self):
        client = Client()
        url = reverse('about')
        response = client.get(url)
        json_response = json.loads(response.content)

        self.assertIsNotNone(json_response['maintenance'])
