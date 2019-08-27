from rest_framework.serializers import ModelSerializer


from .models import List, ListItem


class ListItemSerializer(ModelSerializer):
    class Meta:
        model = ListItem
        fields = ("name", "context", "description")


class ListSerializer(ModelSerializer):
    list_items = ListItemSerializer(many=True)

    class Meta:
        model = List
        fields = ("title", "curator", "list_items")
