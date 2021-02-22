# Generated by Django 3.0.6 on 2020-10-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='music')),
                ('cast', models.CharField(max_length=500)),
                ('genre', models.CharField(choices=[('pop', 'POP'), ('electronic', 'ELECTRONIC'), ('bollywood_romantic', 'BOLLYWOOD ROMANTIC'), ('bollywood_singles', 'BOLLYWOOD SINGLES'), ('country', 'COUNTRY'), ('animated', 'ANIMATED MUSIC VIDEO')], max_length=40)),
                ('imdbrating', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
