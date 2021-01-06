from django.conf.urls import url
from django.contrib import admin
from Employeeincomestatement import views
urlpatterns=[
    #url(r'^login/$',views.login_page), #这将是一个登陆页面。
   #url(r'^p/(?<IDcard>\d+)/$',views.peopleinformationshow),
    #url(r'^templay/$',views.templay),#测试模块
    url(r'^result/$',views.EIS_show_information),#测试模块
]
