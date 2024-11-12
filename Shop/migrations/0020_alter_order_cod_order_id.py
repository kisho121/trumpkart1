# Generated by Django 5.0.6 on 2024-08-17 18:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0019_supportissue_order_cod_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cod_order_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
