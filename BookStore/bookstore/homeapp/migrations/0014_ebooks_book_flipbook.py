# Generated by Django 4.1.1 on 2023-03-01 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0013_alter_ebooks_book_audiofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebooks',
            name='book_flipbook',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]