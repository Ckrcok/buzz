# Generated by Django 3.1.7 on 2021-04-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210407_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_coffee',
            name='favorite_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='admin_coffee',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
