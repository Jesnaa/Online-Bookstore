# Generated by Django 4.1.1 on 2023-04-17 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homeapp', '0019_orderplaced_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='delivery_boy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_delivered', to=settings.AUTH_USER_MODEL),
        ),
    ]
