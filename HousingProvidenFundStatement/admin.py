from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import format_html   

# Register your models here.
from HousingProvidenFundStatement.models import Person,UploadExcel
from django.contrib.auth.models import User
import xlrd
import ast
import os

admin.site.site_header = '华电龙口 人力资源部 后台管理系统'
class PersonAdmin(admin.ModelAdmin):
    list_display = ('IDcard','havelook')
    readonly_fields = ['havelook']
    search_fields = ('IDcard','havelook')

admin.site.register(Person,PersonAdmin)

def get_excel_information(excel_file):
    inputError = "" #存放没有导入人的名单
    file = xlrd.open_workbook(excel_file)
    info=file.sheet_by_index(0)
    print(info.nrows)
    for n in range(info.nrows):
        if '姓名' in str(info.cell(n,0)).split(":")[1]:
            index = n
            name = ast.literal_eval(str(info.cell(index,1)).split(":")[1])
            try:
                IDcard = ast.literal_eval(str(info.cell(index,3)).split(":")[1])
            except:
                IDcard = str(info.cell(index,3)).split(":")[1]
            gongjijinzhanghao =str(info.cell(index,7)).split(":")[1]
            try:
                workaccount = ast.literal_eval(str(info.cell(n-2,1)).split(":")[1])
                workname = ast.literal_eval(str(info.cell(n-2,6)).split(":")[1])
            except ValueError:
                workaccount = str(info.cell(n-2,1)).split(":")[1]
                workname = str(info.cell(n-2,6)).split(":")[1]
            
            deposit_month = str(info.cell(index+1,2)).split(":")[1]

            accumulated_account_balance = str(info.cell(index+2,2)).split(":")[1]
            cumulative_balance = str(info.cell(index+3,2)).split(":")[1]
            #企补累计余额
            qi_bu_cumulative_balance = str(info.cell(index+4,2)).split(":")[1]
            #上年末个缴余额
            balance_at_the_end_of_the_previous_year = str(info.cell(index+5,2)).split(":")[1]
            #上年末企补余额
            qi_ye_at_the_end_of_the_previous_year = str(info.cell(index+6,2)).split(":")[1]
            #上年末个缴利息
            interest_paid_at_the_end_of_the_previous_year = str(info.cell(index+7,2)).split(":")[1]
            #上年末企补利息
            qi_ye_interest_paid_at_the_end_of_the_previous_year = str(info.cell(index+8,2)).split(":")[1]
            #本年个缴金额
            amount_paid_this_year = str(info.cell(index+9,2)).split(":")[1]
            #本年企补金额
            the_amount_of_enterprise_compensation_this_year = str(info.cell(index+10,2)).split(":")[1]
            #本年个缴利息
            interest_paid_this_year = str(info.cell(index+11,2)).split(":")[1]
            #本年企补利息
            this_years_corporate_interest = str(info.cell(index+12,2)).split(":")[1]
            #本年利率
            interest_rate_this_year = str(info.cell(index+13,2)).split(":")[1]
            #上年利率
            last_year_interest_rate = str(info.cell(index+14,2)).split(":")[1]
            #本年提取金额
            this_year_get_money = str(info.cell(index+15,2)).split(":")[1]
            #本年提取日期
            withdrawal_date_this_year = str(info.cell(index+16,2)).split(":")[1]
            #print(accumulated_account_balance,'-------',cumulative_balance)
            #内容
            #缴存月份、个人缴费、企业缴费、记账日期
            #2,2-5
            month_dict = {}
            try:
                if str(info.cell(index+2,5)).split(":")[1]:
                    next_num = index+3
                    month_dict[ast.literal_eval(str(info.cell(index+2,5)).split(":")[1])] = [str(info.cell(index+2,6)).split(":")[1],ast.literal_eval(str(info.cell(index+2,7)).split(":")[1]),ast.literal_eval(str(info.cell(index+2,8)).split(":")[1])]
                    while ("empty" not in str(info.cell(next_num,5))):
                        month_dict[ast.literal_eval(str(info.cell(next_num,5)).split(":")[1])]=[str(info.cell(next_num,6)).split(":")[1],ast.literal_eval(str(info.cell(next_num,7)).split(":")[1]),ast.literal_eval(str(info.cell(next_num,8)).split(":")[1])]
                        next_num += 1
            except ValueError:
                if str(info.cell(index+2,5)).split(":")[1]:
                    next_num = index+3
                    month_dict[str(info.cell(index+2,5)).split(":")[1]] = [str(info.cell(index+2,6)).split(":")[1],str(info.cell(index+2,7)).split(":")[1],str(info.cell(index+2,8)).split(":")[1]]
                    while ("empty" not in str(info.cell(next_num,5))):
                        month_dict[ast.literal_eval(str(info.cell(next_num,5)).split(":")[1])]=[str(info.cell(next_num,6)).split(":")[1],str(info.cell(next_num,7)).split(":")[1],str(info.cell(next_num,8)).split(":")[1]]
                        next_num += 1
           
            if not Person.objects.filter(IDcard=IDcard).exists():
                Person.objects.create(
                        name = name,
                        #user_id=user_id, #去掉这个外键
                        IDcard=IDcard,
                        workaccount =workaccount,
                        workname=workname,
                        gongjijinzhanghao=gongjijinzhanghao,
                        deposit_month=deposit_month,
                        accumulated_account_balance=accumulated_account_balance,
                        cumulative_balance=cumulative_balance,
                        qi_bu_cumulative_balance=qi_bu_cumulative_balance,
                        balance_at_the_end_of_the_previous_year=balance_at_the_end_of_the_previous_year,
                        qi_ye_at_the_end_of_the_previous_year=qi_ye_at_the_end_of_the_previous_year,
                        interest_paid_at_the_end_of_the_previous_year=interest_paid_at_the_end_of_the_previous_year,
                        qi_ye_interest_paid_at_the_end_of_the_previous_year=qi_ye_interest_paid_at_the_end_of_the_previous_year,
                        amount_paid_this_year=amount_paid_this_year,
                        the_amount_of_enterprise_compensation_this_year=the_amount_of_enterprise_compensation_this_year,
                        interest_paid_this_year=interest_paid_this_year,
                        this_years_corporate_interest=this_years_corporate_interest,
                        interest_rate_this_year=interest_rate_this_year,
                        last_year_interest_rate=last_year_interest_rate,
                        this_year_get_money=this_year_get_money,
                        withdrawal_date_this_year=withdrawal_date_this_year,
                        content=month_dict)
        else:
            pass
           # inputError+="%s  %s<\br>"%(name,IDcard)
           
    inputError+="导入数据完成！"
    return inputError

@admin.register(UploadExcel)
class UploadExcel_Admin(admin.ModelAdmin):
    list_display = ['file','check_people']
    fields = ['file','check_people']

    def save_model(self,request,obj,form,change):
        with open('media/hpfs/temp.xls','wb') as fd:
            for chunk in request.FILES['file']:
                fd.write(chunk)

        try:
            get_excel_information('media/hpfs/temp.xls')
            try:
                if request.POST['check_people']:
                    logined = set()
                    persondict = {}
                    for per in User.objects.only():
                        #将会增加身份证号
                        logined.add(per)
                    for y in Person.objects.only():
                        persondict[y.IDcard] = y.name
                    
                    test = set(persondict.keys())
                    print(test)
                    with open('media/download/temp_hpfs.txt','w') as fd:
                        #filecsv = csv.writer(fd)
                        for people in test.difference(logined):
                            #print(people,persondict[people])
                            #filecsv.writerow([people,persondict[people]])
                            fd.write('%s:%s \n'%(people,persondict[people]))
                    message = format_html('下载 <a href="/hpfs/download">没有注册人员名单</a>')
                    self.message_user(request, message,extra_tags='error')

            except:
                self.message_user(request,'名单导入成功！')
        except:
            self.message_user(request, '请导入正确的文件！',  extra_tags='error')
        
        os.remove("media/hpfs/temp.xls")