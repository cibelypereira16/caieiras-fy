# Generated by Django 2.2.5 on 2019-09-06 20:31

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
                ('name_music', models.CharField(max_length=50, verbose_name='name music')),
                ('artist', models.CharField(max_length=255, verbose_name='artist')),
                ('genre', models.CharField(max_length=255, verbose_name='genre')),
                ('link_music', models.CharField(max_length=255, verbose_name='link_music')),
            ],
        ),
    ]
