# Generated by Django 3.0.4 on 2020-04-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samplemodel', '0002_auto_20200417_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='option',
            field=models.BooleanField(default=True),
        ),
    ]