# Generated by Django 5.0.6 on 2024-08-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0021_rename_issue_supportissue_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_order_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
