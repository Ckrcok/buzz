# Generated by Django 3.1.7 on 2021-04-08 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210407_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_coffee',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
