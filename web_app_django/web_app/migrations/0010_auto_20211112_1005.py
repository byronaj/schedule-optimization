# Generated by Django 3.2.9 on 2021-11-12 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_rename_reportresults_reportresult'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContinuousSequenceConstraint',
            new_name='ContinuousSequence',
        ),
        migrations.RenameModel(
            old_name='PenalizedTransitionsConstraint',
            new_name='PenalizedTransitions',
        ),
        migrations.RenameModel(
            old_name='WeeklySumConstraint',
            new_name='WeeklySum',
        ),
        migrations.DeleteModel(
            name='ReportResult',
        ),
    ]
