# Generated by Django 4.0.7 on 2023-06-15 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_file_type_song_song_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_name',
            new_name='genre',
        ),
    ]
