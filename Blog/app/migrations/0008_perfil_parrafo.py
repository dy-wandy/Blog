# Generated by Django 4.2.2 on 2023-06-23 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_perfil_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='parrafo',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
