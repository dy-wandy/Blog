# Generated by Django 4.2.2 on 2023-06-24 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_perfil_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='parrafo',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
    ]
