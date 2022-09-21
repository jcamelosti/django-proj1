from django.urls import path

# from recipes.views import home  # ao inves de importar vários posso importar todas as views de recipes
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="recipes"),  # Home
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
