# Generated by Django 3.0.4 on 2020-04-17 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samplemodel', '0008_auto_20200417_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]