from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import List, ListItem
from .serializers import ListSerializer, ListItemSerializer


class ListCuratedLists(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
    lookup_url_kwarg = "item_id"
