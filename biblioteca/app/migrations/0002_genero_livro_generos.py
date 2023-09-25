# Generated by Django 4.2.4 on 2023-09-25 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='livro',
            name='generos',
            field=models.ManyToManyField(to='app.genero'),
        ),
    ]
