import uuid

from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model for self-updating created/updated fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    An abstract base model that uses a UUID for the models' PK.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
