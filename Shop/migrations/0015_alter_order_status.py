# Generated by Django 5.0.6 on 2024-08-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0014_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Delivered'), (2, 'Canceled')], default=0),
        ),
    ]
