# Generated by Django 3.1.7 on 2021-04-08 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20210408_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_coffee',
            name='description',
        ),
        migrations.RemoveField(
            model_name='user_coffee',
            name='description',
        ),
    ]
