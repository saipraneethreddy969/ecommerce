# Generated by Django 3.0.4 on 2020-06-02 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samplemodel', '0024_auto_20200530_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crops',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samplemodel.Farmer'),
        ),
    ]