# Generated by Django 3.2.9 on 2021-11-12 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0007_reportresults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportresults',
            name='num_weeks',
            field=models.IntegerField(default=2),
        ),
    ]
