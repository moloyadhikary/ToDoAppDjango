# Generated by Django 2.2.5 on 2019-09-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('added_date', models.DateTimeField()),
                ('completed_date', models.DateTimeField(auto_now=True)),
                ('note', models.CharField(max_length=500)),
            ],
        ),
    ]
