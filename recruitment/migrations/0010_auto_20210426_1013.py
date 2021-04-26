# Generated by Django 2.2.20 on 2021-04-26 04:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0009_auto_20210426_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='research_exp',
            old_name='to',
            new_name='To',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 26, 4, 42, 57, 390010, tzinfo=utc)),
        ),
    ]
