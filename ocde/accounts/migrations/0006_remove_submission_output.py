# Generated by Django 3.1.2 on 2020-12-08 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201207_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='output',
        ),
    ]