from django.urls import path
from crud import views 

app_name = "crud"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_data, name="create"),
    path("update/", views.update_data, name="update"),
    path("<int:pk>/delete/", views.delete_data, name="delete"),
]