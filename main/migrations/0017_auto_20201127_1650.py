# Generated by Django 3.1.3 on 2020-11-27 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20201127_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 16, 50, 53, 149123)),
        ),
    ]