# Generated by Django 3.1.4 on 2020-12-23 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employeeincomestatement', '0002_auto_20201222_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='personeis',
            name='IDcard_num',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='personeis',
            name='IDcard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
