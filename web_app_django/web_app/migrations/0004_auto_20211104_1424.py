# Generated by Django 3.2.8 on 2021-11-04 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_alter_employee_fte'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalConstraints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.IntegerField(default=0)),
                ('shift_hard_min', models.IntegerField(default=0)),
                ('shift_soft_min', models.IntegerField(default=0)),
                ('shift_min_penalty', models.IntegerField(default=0)),
                ('shift_soft_max', models.IntegerField(default=0)),
                ('shift_hard_max', models.IntegerField(default=0)),
                ('shift_max_penalty', models.IntegerField(default=0)),
                ('weekly_sum_shift', models.IntegerField(default=0)),
                ('weekly_sum_hard_min', models.IntegerField(default=0)),
                ('weekly_sum_soft_min', models.IntegerField(default=0)),
                ('weekly_sum_min_penalty', models.IntegerField(default=0)),
                ('weekly_sum_soft_max', models.IntegerField(default=0)),
                ('weekly_sum_hard_max', models.IntegerField(default=0)),
                ('weekly_sum_max_penalty', models.IntegerField(default=0)),
                ('previous_shift', models.IntegerField(default=0)),
                ('next_shift', models.IntegerField(default=0)),
                ('penalty', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
