from django.urls import path

from meteo import views

urlpatterns = (
    path("meteo/", views.temp_here, name="temp_here"),
    path("meteo/discover", views.temp_somewhere, name="temp_somewhere"),
    path("meutempo.up.railway.app/", views.temp_somewhere, name="temp_somewhere"),
    path("meutempo.up.railway.app/", views.temp_here, name="temp_here"),
)

