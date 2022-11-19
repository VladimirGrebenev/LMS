from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.hello_world),
    path("<str:word>/", views.check_kwargs),
]