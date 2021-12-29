from django.contrib import admin
from django.urls import path, include
from . import views
from mobile.views import About


urlpatterns = [

    path('product/', views.home_view, name='mobile'),
    path('all/', About.as_view(), name="allselect"),
]
