# Generated by Django 3.1.3 on 2020-11-26 13:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201124_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.hotel'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 19, 16, 43, 300217)),
        ),
    ]
