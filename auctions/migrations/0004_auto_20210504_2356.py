# Generated by Django 3.1.7 on 2021-05-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210504_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to='auctions.Category'),
        ),
    ]
