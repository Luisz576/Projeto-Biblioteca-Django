# Generated by Django 4.2.4 on 2023-09-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_genero_livro_generos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='categoria',
        ),
        migrations.AddField(
            model_name='livro',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
