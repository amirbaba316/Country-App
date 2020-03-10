from django.contrib import admin
from django.urls import path,re_path
from country_app.views import Country_detail,map_view

urlpatterns = [
    path('',Country_detail.as_view(),name="country_detail"),
    re_path(r'^map/$',map_view.as_view(),name="map"),
]
