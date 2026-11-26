from django.urls import path
from . import views

urlpatterns = [
    path("vizitka/", views.du2_vizitka, name="du2_vizitka"),
    path("teplota/", views.du3_teplota, name="du3_teplota"),
]
