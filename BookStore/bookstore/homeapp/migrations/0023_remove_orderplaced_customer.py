# Generated by Django 4.1.1 on 2023-05-13 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0022_alter_orderplaced_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='customer',
        ),
    ]
