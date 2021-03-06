# Generated by Django 3.2.2 on 2021-05-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='byline',
            new_name='Bio',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='body',
            new_name='description',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_instructions',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_required',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
