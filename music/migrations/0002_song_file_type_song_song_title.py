# Generated by Django 4.0.7 on 2023-06-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file_type',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='song',
            name='song_title',
            field=models.CharField(default=0, max_length=50),
        ),
    ]