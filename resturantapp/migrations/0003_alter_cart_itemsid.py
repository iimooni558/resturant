# Generated by Django 4.2.15 on 2024-09-02 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturantapp', '0002_items_price_increase_per_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='itemsid',
            field=models.IntegerField(),
        ),
    ]
