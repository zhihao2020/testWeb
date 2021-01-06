from django.shortcuts import render
from django.http import HttpResponse

from HousingProvidenFundStatement.models import Person

# Create your views here.
def peopleinformationshow(request):
    return HttpResponse('<p>用户展示页</p>')

def HPFS_deal_post(request):
    try:
        ctx = {}
        #这里是通过User的模块，直接通过匹配IDcard和User.username
        if request.user.is_authenticated:
                #user = User.objects.filter(username=request.user.username).values().get()['username']
                #all_information = Person.objects.filter(user_id=user).values().get()
                all_information = Person.objects.filter(IDcard=request.user.username).values().get()
                for k,v in all_information.items():
                    if k == "content":
                        try:
                            ctx[k]=ast.literal_eval(v)
                        except :
                            ctx[k] = ""
                    else:
                        ctx[k]=v    

                return render(request,"showpeopleinformation.html",ctx)
           
        return render(request,"showpeopleinformation.html",ctx)
    except :
        return render(request,"nofind.html")
