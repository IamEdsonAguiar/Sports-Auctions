# Generated by Django 3.2.13 on 2022-10-20 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidPrice', to='auctions.bid'),
        ),
    ]
