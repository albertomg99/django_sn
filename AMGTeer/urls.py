# AMGTeer/urls.py

from django.urls import path
from django.conf.urls import include, url
from .views import dashboard, profile_list, profile, register

app_name = "AMGTeer"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]
