# Generated by Django 3.1.7 on 2021-04-09 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_merge_20210408_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_coffee',
            name='photo',
            field=models.CharField(default='https://i.imgur.com/DXtLJUo.png', max_length=200),
        ),
    ]
