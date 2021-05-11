# Generated by Django 3.1.7 on 2021-05-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='item',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='maker',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='value',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='exists',
            field=models.BooleanField(default=False),
        ),
    ]
