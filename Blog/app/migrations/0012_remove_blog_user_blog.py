# Generated by Django 4.2.2 on 2023-06-24 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_text_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user_blog',
        ),
    ]
