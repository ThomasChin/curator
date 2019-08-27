from django.urls import path


from .views import ListCuratedLists, ListDetail


app_name = "lists"

urlpatterns = [path("", ListCuratedLists.as_view()), path("/<uuid:pk>", ListDetail.as_view())]
