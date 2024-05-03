from django.urls import path
from contact import views

APP_NAME = 'contact'

urlpatterns = [
    path("", views.index, name='index'),
]
