# Generated by Django 5.0.6 on 2024-08-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0011_addressmodel_area_addressmodel_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(choices=[(0, 'Pending'), (1, 'Canceled'), (2, 'Delivered')], default=0),
        ),
    ]