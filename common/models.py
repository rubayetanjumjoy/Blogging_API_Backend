from django.db import models
from django.utils import timezone


class TSFieldsIndexed(models.Model):
    ts_created = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    ts_updated = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    class Meta:
        abstract = True


class TimeFields(models.Model):
    ts_created = models.DateTimeField(default=timezone.now, editable=False)
    ts_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
