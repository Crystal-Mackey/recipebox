from django.contrib import admin


from recipeapp.models import Recipe, Author

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Author)