# Generated by Django 3.2.6 on 2021-09-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=50)),
                ('points', models.IntegerField()),
            ],
        ),
    ]
