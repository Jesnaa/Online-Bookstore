# Generated by Django 4.1.1 on 2022-11-19 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_order_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_item',
            name='quantity',
            field=models.BigIntegerField(default=1),
        ),
    ]
