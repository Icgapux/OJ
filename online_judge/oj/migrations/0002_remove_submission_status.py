# Generated by Django 2.2.7 on 2019-12-20 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='status',
        ),
    ]
