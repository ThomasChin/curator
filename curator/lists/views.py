from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from .models import List, ListItem
from .serializers import ListSerializer, ListItemSerializer


class IsOwnerOrReadOnlyList(BasePermission):
    """
    Object-level permission to only allow owners of a List to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        return obj.curator == request.user


class IsOwnerOrReadOnlyListItem(BasePermission):
    """
    Object-level permission to only allow owners of a ListItem to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        return obj in ListItem.objects.filter(list__curator=request.user)


class ListCuratedLists(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyList]
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyListItem]
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
    lookup_url_kwarg = "item_id"
