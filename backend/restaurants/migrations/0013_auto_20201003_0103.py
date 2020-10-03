# Generated by Django 3.1.2 on 2020-10-03 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0012_auto_20201002_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='deal',
        ),
        migrations.AddField(
            model_name='deal',
            name='items',
            field=models.ManyToManyField(to='restaurants.Item'),
        ),
    ]
