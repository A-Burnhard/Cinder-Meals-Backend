# Generated by Django 4.1.6 on 2023-03-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_order_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
