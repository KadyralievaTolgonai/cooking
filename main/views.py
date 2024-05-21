from django.shortcuts import render,get_list_or_404
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')


def category_detail(request,slug):
    category=Category.objects.get(slug=slug)
    recipes=Recipe.objects.filter(category_id=slug)
    return render(request,'category-detail.html',locals())


def recipe_detail(request,pk):
   
    recipe=get_list_or_404(Recipe,pk=pk)
    # image=recipe.get_image
    # images=recipe.images.exclude(id=image.id)
    return render(request,'recipe-detail.html',locals())

def add_recipe(request):
    return render(request,'add-recipe.html')
