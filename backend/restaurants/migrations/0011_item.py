# Generated by Django 3.1.2 on 2020-10-02 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_remove_deal_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='restaurants.deal')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='restaurants.restaurant')),
            ],
        ),
    ]
