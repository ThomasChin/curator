from django.urls import path

from .views import ListCuratedLists, ListDetail, ListItemDetail

app_name = "lists"

urlpatterns = [
    path("", ListCuratedLists.as_view()),
    path("<uuid:pk>/", ListDetail.as_view()),
    path("<uuid:pk>/items/<uuid:item_id>/", ListItemDetail.as_view()),
]
