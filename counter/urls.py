from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("contador/", views.async_time_counter, name="async-counter"),
]
