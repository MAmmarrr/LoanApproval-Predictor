
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views as v

app_name='main'
urlpatterns = [
    path('home/', v.index, name="index"),
    path('', v.index, name="index"),
    path('form/', v.request_loan),
    path('result/',v.prediction)
]
