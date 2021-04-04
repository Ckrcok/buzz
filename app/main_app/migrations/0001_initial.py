# Generated by Django 3.1.7 on 2021-04-03 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('cof_type', models.CharField(choices=[('C', 'Cafe Bought'), ('S', 'Store Bought Home Made')], default='C', max_length=2, verbose_name='type')),
                ('categories', models.CharField(choices=[('C', 'Cold Coffee'), ('D', 'Decaffeinated'), ('IC', 'Iced Coffe'), ('R', 'Regular Coffe')], default='C', max_length=2, verbose_name='categories')),
                ('photo', models.ImageField(upload_to='coffee')),
                ('rating', models.IntegerField()),
                ('Favorites', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatar')),
                ('admincof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.admin_coffee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Coffe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('cof_type', models.CharField(choices=[('C', 'Cafe Bought'), ('S', 'Store Bought Home Made')], default='C', max_length=2, verbose_name='type')),
                ('categories', models.CharField(choices=[('C', 'Cold Coffe'), ('D', 'Decaffeinated'), ('IC', 'Iced Coffe'), ('R', 'Regular Coffe')], default='C', max_length=2, verbose_name='categories')),
                ('photo', models.ImageField(upload_to='coffee')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.admin_coffe')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='usercof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.user_coffee'),
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffee', models.ManyToManyField(to='main_app.Admin_Coffe')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
    ]
