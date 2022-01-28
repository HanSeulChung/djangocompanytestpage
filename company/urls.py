"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views

#app_name='Departments', 'Employers'
# app_name1= 'departments'
# app_name2= 'employers'

app_name='company'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('department/reg/',views.regDepartment, name='regD'),
    path('department/regCon/', views.regConDepartment, name='regConD'),
    path('department/all/', views.reaDepartmentAll, name='depAll'),
    path('department/<str:pk>det/',views.detDepartment,name='depDet'),
    path('department/<str:pk>mod/',views.modDepartmentOne,name='depMod'),
    path('departemnt/modCon/',views.modConDepartment,name='modConD'),
    path('department/<str:pk>del/',views.delConDepartment, name='depDel'),

    path('employer/reg/',views.regEmployer, name='regE'),
    path('employer/regCon/', views.regConEmployer, name='regConE'),
    path('employer/all/', views.reaEmployerAll, name='empAll'),
    path('employer/<str:ID>det/',views.detEmployer,name='empDet'),
    path('employer/<str:ID>mod/',views.modEmployerOne,name='empMod'),
    path('employer/modCon/',views.modConEmployer,name='modConE'),
    path('employer/<str:ID>del/',views.delConEmployer, name='empDel'),

    path('admin/', admin.site.urls),
]
