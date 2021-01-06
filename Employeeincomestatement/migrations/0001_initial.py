# Generated by Django 3.1.4 on 2020-12-22 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonEIS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='姓名')),
                ('account', models.CharField(max_length=200, verbose_name='工号')),
                ('month_start', models.CharField(max_length=200, verbose_name='起始月')),
                ('month_end', models.CharField(max_length=200, verbose_name='终止月')),
                ('sum_salary', models.CharField(max_length=200, verbose_name='年工资总额')),
                ('month_salary', models.CharField(max_length=200, verbose_name='月平均工资')),
                ('signature', models.CharField(max_length=200, verbose_name='本人签字')),
                ('comments', models.CharField(max_length=200, verbose_name='备注')),
                ('IDcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='身份证')),
            ],
            options={
                'verbose_name': '职工收入账单表',
                'verbose_name_plural': '职工收入账单表',
            },
        ),
    ]