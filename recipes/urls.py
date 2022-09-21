from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# from recipes.views import home  # ao inves de importar vários posso importar todas as views de recipes
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="recipes"),  # Home
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
