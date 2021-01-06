from django.conf.urls import url
from django.contrib import admin
from HousingProvidenFundStatement import views
urlpatterns=[
    #url(r'^login/$',views.login_page), #这将是一个登陆页面。
   #url(r'^p/(?<IDcard>\d+)/$',views.peopleinformationshow),
    #url(r'^templay/$',views.templay),#测试模块
    url(r'^result/$',views.HPFS_deal_post),#测试模块

]
