from django.urls import path

#from recipes.views import home  # ao inves de importar vários posso importar todas as views de recipes
from . import views

urlpatterns = [
    path('', views.home), #Home
    path('recipes/<int:id>/', views.recipe), #detalhes
]
