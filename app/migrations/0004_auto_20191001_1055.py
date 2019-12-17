# Generated by Django 2.2.5 on 2019-10-01 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190930_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='note',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]