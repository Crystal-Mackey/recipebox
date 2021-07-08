from django.shortcuts import render

from recipeapp.models import Recipe, Author

# Create your views here.
def index(request):
    posts = Recipe.objects.all()
    return render(request, 'index.html', {'posts': posts})


def recipe_detail(request, post_id: int):
    post = Recipe.objects.get(id=post_id)
    return render(request, 'recipe_detail.html', {'post': post})


def author_detail(request, author_id: int):
    my_author = Author.objects.get(id=author_id)
    author_recipe = Recipe.objects.filter(author=my_author)
    return render(request, 'author_detail.html', {'author': my_author, 'recipe':author_recipe})
