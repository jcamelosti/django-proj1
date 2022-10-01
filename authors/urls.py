from django.urls import path

from . import views

app_name = 'authores'

urlpatterns = [
    path('register/', views.register_view, name="register_view"),
]
