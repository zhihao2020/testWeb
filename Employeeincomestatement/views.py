from django.shortcuts import render
#from HousingProvidenFundStatement.forms import ExcelForm

from Employeeincomestatement.models import PersonEIS

# Create your views here.

def EIS_show_information(request):
    try:
        ctx = {}
        if request.user.is_authenticated:
            #user = User.objects.filter(username=request.user.username).values().get()['username']
            information_eis = PersonEIS.objects.filter(IDcard_num=request.user.username).values().get()
            for k,v in information_eis.items():
                ctx[k]=v
            
            #增加判断用户是否查看功能
            temp = PersonEIS.objects.get(IDcard_num=request.user.username)
            temp.havelook = '是'
            temp.save()
            return render(request,"showEmployeeIncomeStatement.html",ctx)
        return render(request,"showEmployeeIncomeStatement.html",ctx)
    except:
        return render(request,"nofind.html")