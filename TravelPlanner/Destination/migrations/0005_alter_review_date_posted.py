# Generated by Django 4.2.6 on 2023-12-28 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Destination', '0004_review_destination_alter_review_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
