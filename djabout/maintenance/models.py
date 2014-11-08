from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from .validators import has_valid_date


@python_2_unicode_compatible
class MaintenanceMessage(models.Model):
    planned_date = models.DateTimeField(validators=[has_valid_date])
    reason = models.CharField(max_length=100)

    def __str__(self):
        return "Planned: %s\nReason: %s" % (
            self.planned_date, self.reason)
