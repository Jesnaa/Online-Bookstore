# Generated by Django 4.1.1 on 2023-04-30 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0006_address_first_name_address_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]