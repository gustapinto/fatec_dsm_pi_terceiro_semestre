from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name ="dashb"

urlpatterns = [
    path("", login_required(views.DashbView.as_view()), name="dashb"),
]