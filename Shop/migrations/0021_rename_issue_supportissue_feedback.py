# Generated by Django 5.0.6 on 2024-08-17 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0020_alter_order_cod_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supportissue',
            old_name='issue',
            new_name='feedback',
        ),
    ]
