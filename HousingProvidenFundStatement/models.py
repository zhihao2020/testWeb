"""
Created by zhihao
2020.12.31 change the models(delete user_id to complish dividend)
"""
from django.db import models
from django import forms
from django.contrib.auth.models import User
from website import settings

# Create your models here.
class Person(models.Model):
    #user=models.ForeignKey(User,verbose_name="用户",on_delete=models.CASCADE)
    name = models.CharField(max_length=200,verbose_name="姓名",default="")
    IDcard=models.CharField(max_length=200,verbose_name='身份证')
    workaccount = models.CharField(max_length=200,verbose_name="单位账号",blank=True,null=True,default="")
    workname = models.CharField(max_length=200,verbose_name="单位名称",blank=True,null=True,default="")
    gongjijinzhanghao=models.CharField(max_length=200,verbose_name='公积金账号',blank=True,null=True,default="")
    #缴存月份
    deposit_month = models.CharField(max_length=200,verbose_name="缴存月份",blank=True,null=True,default="")
    #账号累计余额
    accumulated_account_balance = models.CharField(max_length=200,verbose_name='账号累计余额',blank=True,null=True,default="")
    #个缴累计余额
    cumulative_balance = models.CharField(max_length=200,verbose_name='个缴累计余额',blank=True,null=True,default="")
    #企补累计余额
    qi_bu_cumulative_balance = models.CharField(max_length=200,verbose_name='企补累计余额',blank=True,null=True,default="")
    #上年末个缴余额
    balance_at_the_end_of_the_previous_year = models.CharField(max_length=200,verbose_name='上年末个缴余额',blank=True,null=True,default="")
    #上年末企补余额
    qi_ye_at_the_end_of_the_previous_year = models.CharField(max_length=200,verbose_name='上年末企补余额',blank=True,null=True,default="")
    #上年末个缴利息
    interest_paid_at_the_end_of_the_previous_year = models.CharField(max_length=200,verbose_name='上年末个缴利息',blank=True,null=True,default="")
    #上年末企补利息
    qi_ye_interest_paid_at_the_end_of_the_previous_year = models.CharField(max_length=200,verbose_name='上年末企补利息',blank=True,null=True,default="")
    #本年个缴金额
    amount_paid_this_year = models.CharField(max_length=200,verbose_name='本年个缴金额',blank=True,null=True,default="")
    #本年企补金额
    the_amount_of_enterprise_compensation_this_year = models.CharField(max_length=200,verbose_name='本年企补金额',blank=True,null=True,default="")
    #本年个缴利息
    interest_paid_this_year = models.CharField(max_length=200,verbose_name='本年个缴利息',blank=True,null=True,default="")
    #本年企补利息
    this_years_corporate_interest = models.CharField(max_length=200,verbose_name='本年企补利息',blank=True,null=True,default="")
    #本年利率
    interest_rate_this_year = models.CharField(max_length=200,verbose_name='本年利率',blank=True,null=True,default="")
    #上年利率
    last_year_interest_rate = models.CharField(max_length=200,verbose_name='上年利率',blank=True,null=True,default="")
    #本年提取金额
    this_year_get_money = models.CharField(max_length=200,verbose_name='本年提取金额',blank=True,null=True,default="")
    #本年提取日期
    withdrawal_date_this_year = models.CharField(max_length=200,verbose_name='本年提取日期',blank=True,null=True,default="")
    #月份详细信息 
    #缴费月份、个人缴费、企业缴费、记账日期
    content = models.TextField(verbose_name='每月详细信息',blank=True,null=True,default="")

    havelook = models.CharField(max_length=100,verbose_name="是否查看",blank=True,null=True,default="否")

    def __str__(self):
        return str(self.IDcard)
    class Meta:
        verbose_name = "住房公积金个人账户对账单"
        verbose_name_plural = verbose_name
        
class UploadExcel(models.Model):
    #filename = models.CharField(max_length=100)
    file = models.FileField(verbose_name='上传Excel')
    check_people = models.BooleanField(default=False,verbose_name="检查谁没有注册")

    def __str__(self):
        return '临时文件'

    class Meta:
        verbose_name = "上传住房公积金对账单Excel"
        verbose_name_plural = verbose_name