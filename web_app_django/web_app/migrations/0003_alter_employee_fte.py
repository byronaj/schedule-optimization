# Generated by Django 3.2.8 on 2021-11-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_auto_20211031_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='fte',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
