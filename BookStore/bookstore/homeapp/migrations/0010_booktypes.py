# Generated by Django 4.1.1 on 2023-02-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0009_remove_book_slug_remove_category_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTypes',
            fields=[
                ('booktype_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_types', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
