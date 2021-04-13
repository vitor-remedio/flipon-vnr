from django.urls import path

from .views import index, contato, curriculo

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('curriculo', curriculo),
]