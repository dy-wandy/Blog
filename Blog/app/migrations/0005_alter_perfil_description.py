# Generated by Django 4.2.2 on 2023-06-23 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_perfil_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='description',
            field=models.CharField(blank=True, default='Hola! soy Wandy este es mi blog, puedes crear tu propio blog para compartir tus ideas', max_length=1000),
        ),
    ]
