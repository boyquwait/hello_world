from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path("", home.as_view(), name = "home"),
    path("", views.home_1, name="home_1"),
    path("about/", views.about, name="about"),
]