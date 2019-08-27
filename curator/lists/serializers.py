from rest_framework.serializers import ModelSerializer


from .models import List, ListItem


class ListSerializer(ModelSerializer):
    class Meta:
        model = List
        fields = ("title", "curator")


class ListItemSerializer(ModelSerializer):
    class Meta:
        model = ListItem
        fields = '__all__'
