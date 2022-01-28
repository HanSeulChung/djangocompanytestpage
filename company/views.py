from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Department, Employer

from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

# department
def regDepartment(request):
    return render(request,'dept/registerDepartment.html')

def regConDepartment(request):
    ID = str(request.POST['ID'])
    NAME = request.POST['NAME']

    qs = Department(Department_ID=ID, Department_NAME=NAME)
    qs.save()

    return HttpResponseRedirect(reverse('company:depAll'))

def reaDepartmentAll(request):
    qs = Department.objects.all()
    context ={
        'department_list': qs}
    return render(request,'dept/readDepartment.html',context)

def detDepartment(request,pk):

    qs = Department.objects.get(Department_ID=pk)
    context = {'department_info': qs}
    return render(request,'dept/detailDepartment.html',context)

def modDepartmentOne(request,pk):
    qs = Department.objects.get(Department_ID=pk)
    context = {'department_info': qs}
    return render(request, 'dept/modifyDepartment.html',context)

def modConDepartment(request):
    ID = str(request.POST['ID'])
    NAME = request.POST['NAME']

    d_qs = Department.objects.get(Department_ID=ID)

    d_qs.Department_ID= ID
    d_qs.Department_NAME =NAME

    d_qs.save()

    return HttpResponseRedirect(reverse('company:depAll'))

def delConDepartment(request, pk):
    d_qs = Department.objects.get(Department_ID=pk)

    d_qs.delete()
    return HttpResponseRedirect(reverse('company:depAll'))


# employer

def regEmployer(request):
    return render(request,'emp/registerEmployer.html')

def regConEmployer(request):
    ID = str(request.POST['ID'])
    NAME = request.POST['NAME']
    GENDER = request.POST['GENDER']
    age = request.POST['age']
    depID = str(request.POST['depID'])
    DATE = request.POST['DATE']
    IMAGE = request.GET['IMAGE']
    upload = request.POST['upload']

    qs = Employer(Employer_ID=ID, Department_ID= depID,
                  Employer_NAME=NAME,
                  Employer_GENDER=GENDER, Employer_age=age,
                  Date_of_Join=DATE, Photo_Image=IMAGE, upload_at=upload)
    qs.save()

    return HttpResponseRedirect(reverse('company:empAll'))

def reaEmployerAll(request):
    qs = Employer.objects.all()
    context ={'employer_list':qs}
    return render(request,'emp/readEmployer.html',context)

def detEmployer(request,ID):
    qs = Employer.objects.get(Employer_ID=ID)
    context = {'employer_info':qs}
    return render(request,'emp/detailEmployer.html',context)

def modEmployerOne(request,ID):
    qs =Employer.objects.get(Employer_ID=ID)
    context = {'employer_info': qs}
    return render(request, 'emp/modifyEmployer.html',context)

def modConEmployer(request):
    ID = str(request.POST['ID'])
    NAME = request.POST['NAME']
    GENDER = request.POST['GENDER']
    age = request.POST['age']
    depID = str(request.POST['depID'])
    DATE = request.POST['DATE']
    IMAGE = request.GET['IMAGE']
    upload = request.POST['upload']

    e_qs = Employer.objects.get(Employer_ID=ID)

    e_qs.Employer_ID= ID
    e_qs.Employer_NAME =NAME
    e_qs.Employer_GENDER = GENDER
    e_qs.Employer_age = age
    e_qs.Department= depID
    e_qs.Date_of_Join = DATE
    e_qs.Photo_Image = IMAGE
    e_qs.upload_at = upload

    e_qs.save()

    return HttpResponseRedirect(reverse('company:empAll'))

def delConEmployer(request, ID):
    e_qs = Employer.objects.get(Employer_ID=ID)

    e_qs.delete()
    return HttpResponseRedirect(reverse('company:empAll'))
