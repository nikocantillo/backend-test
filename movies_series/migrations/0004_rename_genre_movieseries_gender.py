# Generated by Django 4.1.4 on 2023-05-03 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_series', '0003_gender_created_by_gender_created_in_gender_deleted_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieseries',
            old_name='genre',
            new_name='gender',
        ),
    ]
