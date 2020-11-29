# Generated by Django 3.1.3 on 2020-11-29 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20201128_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 19, 54, 6, 652431)),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - Trash'), (2, '2 - Ok'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Perfect')]),
        ),
    ]