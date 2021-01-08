# -*- coding:utf-8 -*-
from django.http import HttpResponse,JsonResponse,FileResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import auth
from django.contrib.auth.models import User

import re,os

def first_page(request):
    if os.path.exists('media/download/temp_eis.txt'):
        os.remove('media/download/temp_eis.txt')
    if os.path.exists('media/download/temp_hpfs.txt'):
        os.remove('media/download/temp_hpfs.txt')
    return render(request,'index.html')

def page_not_found(request, exception):
    return render(request, '404.html', exception)

def register(request):
    if request.method == "GET":    
        request.session['login_from'] = request.META.get('HTTP_REFERER','/')
        return render(request,'register.html',locals())
    elif request.method=="POST":
        IDcard = request.POST.get('IDcard','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2','')#用于确定两次密码是否一致
        
        last_name = request.POST.get('last_name','')
        if IDcard!='' and password!='' and last_name!="" and password2 !='':
            pattern = re.compile(r'[a-zA-Z0-9]{18}') 
            #检测身份证号是否为18位
            if pattern.match(IDcard):
                if password == password2:
                    if User.objects.filter(username=IDcard).exists() == False:
                        user = User.objects.create_user(username=IDcard,password=password,last_name=last_name)
                        user.save()
                        return redirect('/login/')
                    else:
                        return render(request,'register.html',{'errormsg':'该身份证号 已存在，如忘记密码请联系人力资源部修改。'})      
                else:
                    return render(request,'register.html',{'errormsg':'两次输入密码不相同！'})
            else:      
                return render(request,'register.html',{'errormsg':'请输入18位身份证号！'})
        else:
            return render(request,'register.html',{'errormsg':'身份证、密码和姓名不能为空！'})
  
def login(request):
    ctx = {}
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER','/'))
    else:
        if request.method == "GET":
            request.session['login_from'] = request.META.get('HTTP_REFERER','/')
            return render(request,'login.html',locals())
        elif request.method == 'POST':
            username = request.POST.get('IDcard','')
            password = request.POST.get('password','')
            if username != "" and password != "":
                if User.objects.filter(username=username).exists():
                    user = authenticate(username=username,password=password)
                   
                    if user :
                        auth.login(request,user)
                        print("登录成功")
                        return redirect('/')
                    else:
                        ctx['errormsg'] = "密码错误"
                        return render(request,'login.html',ctx)
                else:
                    ctx['errormsg'] = "用户名不存在"
                    return render(request,'login.html',ctx)
            else:
                ctx['errormsg'] = "用户名和密码不能为空！"
                return render(request,'login.html',ctx)
        else:
            return JsonResponse({"e":"none"})
    
def logOut(request):
    logout(request)
    return redirect("/")

def hpfs_download(request):
    if request.user.is_authenticated:
        try:
            response = FileResponse(open('media/download/temp_hpfs.txt', 'rb'))
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=名单.txt'
            return response
        except Exception:
            return HttpResponse('<p>下载出错了!</p>')

    else:
        return HttpResponse('<p>您没有权限!</p>')

def eis_download(request):
    if request.user.is_authenticated:
        try:
            response = FileResponse(open('media/download/temp_eis.txt', 'rb'))
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=名单.txt'
            return response
        except Exception:
            return HttpResponse('<p>下载出错了!</p>')

    else:
        return HttpResponse('<p>您没有权限!</p>')

