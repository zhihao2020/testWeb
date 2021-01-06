# Generated by Django 3.1.4 on 2020-12-21 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HousingProvidenFundStatement', '0006_auto_20201220_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': '住房公积金个人账户对账单', 'verbose_name_plural': '住房公积金个人账户对账单'},
        ),
        migrations.AlterModelOptions(
            name='upload_user',
            options={'verbose_name': '解析住房公积金个人账户对账单Excel', 'verbose_name_plural': '解析住房公积金个人账户对账单Excel'},
        ),
        migrations.AddField(
            model_name='person',
            name='workaccount',
            field=models.CharField(default=3, max_length=200, verbose_name='单位账号'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='workname',
            field=models.CharField(default=4, max_length=200, verbose_name='单位名称'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]