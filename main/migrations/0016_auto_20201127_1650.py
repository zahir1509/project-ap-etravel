# Generated by Django 3.1.3 on 2020-11-27 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20201126_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 16, 50, 30, 902379)),
        ),
    ]
