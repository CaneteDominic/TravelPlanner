# Generated by Django 4.2.6 on 2023-12-26 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Destination', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2023, 12, 26, 21, 17, 34, 220846)),
        ),
    ]
