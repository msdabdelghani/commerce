# Generated by Django 3.1.7 on 2021-04-08 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=555)),
                ('initialprice', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('status', models.CharField(choices=[('Y', 'Your bid is the current bid'), ('N', '')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=555)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('auctions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_listing', to='auctions.auction')),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='bids',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='auctions.bid'),
        ),
        migrations.AddField(
            model_name='auction',
            name='comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_comments', to='auctions.comment'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_auctions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_auctions', to='auctions.auction'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_bids',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_bids', to='auctions.bid'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='auctions.comment'),
        ),
    ]
