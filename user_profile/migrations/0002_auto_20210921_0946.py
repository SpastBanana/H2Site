# Generated by Django 3.1.7 on 2021-09-21 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='delta_ids',
            new_name='meting_ids',
        ),
    ]