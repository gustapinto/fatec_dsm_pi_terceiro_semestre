from django.urls import path
from . import views

app_name ="configurat"

urlpatterns = [
    path("",views.ConfiguratView.as_view(), name="configurat"),
]