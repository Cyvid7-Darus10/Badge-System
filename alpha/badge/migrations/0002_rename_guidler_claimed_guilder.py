# Generated by Django 3.2.6 on 2021-09-04 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claimed',
            old_name='guidler',
            new_name='guilder',
        ),
    ]
