# Generated by Django 3.1.4 on 2020-12-21 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HousingProvidenFundStatement', '0007_auto_20201221_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='pwd',
        ),
    ]
