from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import DatabaseError
from django.http import JsonResponse

from .models import MaintenanceMessage


def about(request):
    json_data = {
        'version': settings.APP_VERSION,
        'maintenance': None,
        'database': 'ok'
    }

    try:
        maintenance = MaintenanceMessage.objects.last()
        if maintenance:
            json_data['maintenance'] = maintenance.reason + \
                " " + str(maintenance.planned_date)
    except (DatabaseError, ImproperlyConfigured):
        json_data['database'] = 'Not Available'
    return JsonResponse(json_data)
