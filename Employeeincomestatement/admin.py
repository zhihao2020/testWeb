from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import format_html  
# Register your models here.
from Employeeincomestatement.models import PersonEIS,UploadExcel
from django.contrib.auth.models import User
import xlrd
import ast
import os
import secrets

# Register your models here.
admin.site.site_header = '华电龙口 人力资源部 后台管理系统'

def get_excel_information(excel_file):
    file = xlrd.open_workbook(excel_file)
    info=file.sheet_by_index(0)
    #print(str(info.cell(3,0)).split(":")[1])
   
    for n in range(info.nrows):
        #print(str(info.cell(n,0)).split(":")[1])
        if '工号' not in str(info.cell(n,0)).split(":")[1]:
            try:
                account = ast.literal_eval(str(info.cell(n,0)).split(":")[1])
            except ValueError:    
                account = str(info.cell(n,0)).split(":")[1]
            try:
                name = ast.literal_eval(str(info.cell(n,1)).split(":")[1])
            except ValueError:
                name = str(info.cell(n,1)).split(":")[1]
            try:
                IDcard_num = ast.literal_eval(str(info.cell(n,3)).split(":")[1])
            except ValueError:
                IDcard_num = str(info.cell(n,3)).split(":")[1]
            try:
                sum_salary = ast.literal_eval(str(info.cell(n,4)).split(":")[1])
            except ValueError:
                sum_salary = str(info.cell(n,4)).split(":")[1]
            try:
                month_salary = ast.literal_eval(str(info.cell(n,5)).split(":")[1])
            except ValueError: 
                month_salary = str(info.cell(n,5)).split(":")[1]
                
            month_flag = str(info.cell(n,6)).split(":")[1]
            if "SPICAL" in month_flag:
                try:
                    month_start = ast.literal_eval(str(info.cell(n,7)).split(":")[1])
                except ValueError:
                    month_start = str(info.cell(n,7)).split(":")[1]
                try:
                    month_end = ast.literal_eval(str(info.cell(n,8)).split(":")[1])
                except ValueError:
                    month_end = str(info.cell(n,8)).split(":")[1]
            else:
                month_start = "1"
                month_end = "12"
            if not PersonEIS.objects.filter(IDcard_num=IDcard_num).exists():
                PersonEIS.objects.create(
                        name = name,
                        IDcard_num=IDcard_num,
                        #IDcard_id = user_id,
                        account=account,
                        sum_salary=sum_salary,
                        month_salary=month_salary,
                        month_start=month_start,
                        month_end=month_end
                    )
            else:
                pass

@admin.register(UploadExcel)
class UploadExcel_Admin(admin.ModelAdmin):
    list_display = ['file','check_people']
    fields = ['file','check_people']

    def save_model(self,request,obj,form,change):
        with open('media/eis/temp.xls','wb') as fd:
            for chunk in request.FILES['file']:
                fd.write(chunk)
        try:
            get_excel_information('media/eis/temp.xls')
            try:
                if request.POST['check_people']:
                    logined = set()
                    persondict = {}
                    for per in User.objects.only():
                        #将会增加身份证号
                        logined.add(per.get_username())

                    for y in PersonEIS.objects.only():
                        persondict[y.IDcard_num] = y.name
                    test = set(persondict.keys())
                  
                    with open('media/download/temp_eis.txt','w') as fd:
                        for people in test.difference(logined):
                            fd.write('%s:%s \n'%(people,persondict[people]))
                    
                    message = format_html('下载 <a href="/eis/Pxym7N2zJR56">没有注册人员名单</a>')
                    self.message_user(request, message, extra_tags='error')
            except:
                self.message_user(request,'名单导入成功！')
        except:
           self.message_user(request, '请导入正确的文件！',  extra_tags='error')
        
        os.remove("media/eis/temp.xls")

class PersonEISAdmin(admin.ModelAdmin):
    readonly_fields = ['havelook']
    list_display = ('IDcard_num','havelook')
    search_fields = ('IDcard_num','havelook')
   
admin.site.register(PersonEIS,PersonEISAdmin)