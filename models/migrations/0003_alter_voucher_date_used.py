# Generated by Django 4.0.5 on 2022-06-23 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_voucher_date_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='date_used',
            field=models.DateTimeField(null=True),
        ),
    ]
