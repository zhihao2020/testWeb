# Generated by Django 3.1.4 on 2020-12-30 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HousingProvidenFundStatement', '0015_person_deposit_month'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upload_user',
            options={'verbose_name': '上传Excel账号', 'verbose_name_plural': '上传Excel账号'},
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='姓名'),
        ),
    ]
