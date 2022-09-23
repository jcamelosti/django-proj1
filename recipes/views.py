#from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe

# from utils.recipes.factory import make_recipe



def home(request):
    recipes = Recipe.objects.all().filter(
            is_published=True,
        ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    #recipes = Recipe.objects.filter(
    #    category__id=category_id
    #).order_by('-id')

    #if not recipes:
    #    raise Http404('Página não encontrada.')

    #return render(request, 'recipes/pages/category.html', context={
    #    'recipes': recipes,
    #    'title': f'{recipes.first().category.name} - Category | '
    #})
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id):
    #recipe = Recipe.objects.get(pk=id)
    #recipe = Recipe.objects.filter(
    #    pk=id,
    #    is_published=True,
    #).order_by('-id').first()
    
    recipe = get_object_or_404(Recipe.objects.filter(
        pk=id,
        is_published=True,
    ))
    
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

def search(request):
     return render(request, 'recipes/pages/search.html')
