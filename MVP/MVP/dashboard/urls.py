from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("uploadreles/", views.uploadreles, name="uploadreles"),
    path("uploaddatacheck/", views.uploaddatacheck, name="uploaddatacheck")
]

