from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import List
from .serializers import ListSerializer

class ListCuratedLists(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = List.objects.all()
