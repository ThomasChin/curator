from django.db import models

from curator.models import TimeStampedModel, UUIDModel
from curator.users.models import User


class List(TimeStampedModel, UUIDModel):
    """
    A model that represents a curated List of ListItems, created by a User.
    """

    title = models.CharField(max_length=128)
    curator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")

    class Meta:
        unique_together = (("title", "curator"),)


class ListItem(TimeStampedModel, UUIDModel):
    """
    A model that represents a single element in a curated List.
    """

    name = models.CharField(max_length=128)
    context = models.CharField(max_length=256, null=True)
    description = models.TextField(max_length=1028, null=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="list_items")
