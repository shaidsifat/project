from django.contrib import admin
from django.urls import path, include
from . import views
from mobile.views import EmployeeUpdate
from mobile.views import home
urlpatterns = [

    path('product/', views.home_view, name='mobile'),
    path('update/<int:pk>/', EmployeeUpdate.as_view(), name='EmployeeUpdate'),
    path('home/', home.as_view(), name='home')
]
