# Generated by Django 4.1.5 on 2024-04-26 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
