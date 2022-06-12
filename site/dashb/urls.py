from django.urls import path
from . import views

app_name ="dashb"

urlpatterns = [
    path("",views.DashbView.as_view(), name="dashb"),
]