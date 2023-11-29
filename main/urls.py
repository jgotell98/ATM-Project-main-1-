from django.urls import path
from . import views

#urlpatterns paths

urlpatterns = [
    path('', views.index, name='index')
]