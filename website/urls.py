"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from website import views

handler404 = views.page_not_found

urlpatterns = [
    path('HR/admin/', admin.site.urls),
    url(r'^$', views.first_page,name="roothome"),
    url(r'^HPFS/',include('HousingProvidenFundStatement.urls')),
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^logout/$',views.logOut,name="logout"),
    url(r'^EIS/',include('Employeeincomestatement.urls')),
    url(r'^hpfs/download/$',views.hpfs_download),
    url(r'^eis/download/$',views.eis_download),
]
