# Generated by Django 2.2.20 on 2021-05-10 05:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0004_auto_20210509_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 5, 10, 5, 34, 50, 399277, tzinfo=utc)),
        ),
    ]