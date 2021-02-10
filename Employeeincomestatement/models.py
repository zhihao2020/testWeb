from django.db import models
from website import settings

# Create your models here.
class PersonEIS(models.Model):
    name = models.CharField(max_length=200,verbose_name="姓名",blank=True,null=True,default="")

    account = models.CharField(max_length=200,verbose_name="工号",blank=True,null=True,default="")

    #取消从User中的外键约束
    # IDcard = models.ForeignKey(User,verbose_name="用户",on_delete=models.CASCADE,blank=True,null=True,default="")
    
    IDcard_num = models.CharField(max_length=200,verbose_name="身份证号",blank=True,null=True,default="")

    month_start = models.CharField(max_length=200,verbose_name="起始月",blank=True,null=True,default="")

    month_end = models.CharField(max_length=200,verbose_name="终止月",blank=True,null=True,default="")

    sum_salary = models.CharField(max_length=200,verbose_name="年工资总额",blank=True,null=True,default="")

    month_salary = models.CharField(max_length=200,verbose_name="月平均工资",blank=True,null=True,default="")

    signature = models.CharField(max_length=200,verbose_name="本人签字",blank=True,null=True,default=" ")

    comments = models.CharField(max_length=200,verbose_name="备注",blank=True,null=True,default=" ")

    havelook = models.CharField(max_length=100,verbose_name="是否查看",blank=True,null=True,default="否")

    def __str__(self):
        return str(self.IDcard_num)
    
    class Meta:
        verbose_name = "职工收入账单表"
        verbose_name_plural = verbose_name

class UploadExcel(models.Model):
    #filename = models.CharField(max_length=100)
    file = models.FileField(verbose_name='上传Excel')
    check_people = models.BooleanField(default=False,verbose_name="检查谁没有注册")

    def __str__(self):
        return '临时文件'

    class Meta:
        verbose_name = "上传职工收入对账单Excel"
        verbose_name_plural = verbose_name