# Generated by Django 4.1.1 on 2022-11-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0002_rename_user_id_user_id_user_groups_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
