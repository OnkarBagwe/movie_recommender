# Generated by Django 3.1.3 on 2020-11-06 08:26

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_auto_20201023_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyRecommender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=600, size=None)),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
    ]
