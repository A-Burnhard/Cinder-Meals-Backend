# Generated by Django 4.1.6 on 2023-03-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
