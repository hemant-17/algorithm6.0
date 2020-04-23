from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
def lockhome(request):
    return render(request,'lockhome.html')

def sign(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password1= request.POST.get('password1','')
        password2= request.POST.get('password2','')


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'USERNAME already registered ')
                return redirect('/sign')

            else:
                user = User.objects.create_user( first_name=first_name,last_name=last_name, username=username, email=email, password=password1 )
                user.save()
                # com= company()
                # com.company_name=first_name
                # com.email=email
                # com.save()
                return redirect('/lock')

        else:
            messages.info(request, 'Confirm password did not match ')
            return redirect('/sign')

    return render(request,'sign1.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        User=auth.authenticate(username=username,password=password)

        if User is not None:
            auth.login(request,User)
            username=request.user.username
            return redirect("/lock")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/login')
    return render(request,'login1.html')

def logout(request):
    auth.logout(request)

    return redirect("/lock")

def post_a_job(request):
    #print(job_offers.company_id)
    resp = company.objects.get(company_id=request.user.profile.company_id)
    print(resp)
    #print(request.user.profile.company_id)
    if request.method=='POST':

        int1=[]
        for i in range(1,7):
            if  (request.POST.get('input'+str(i),'NONE') != 'NONE'):
                int1.append(request.POST.get('input'+str(i),'NONE'))

        int2=[]
        for i in range(1,7):
            if  (request.POST.get('input'+str(i),'NONE') != 'NONE'):
                int2.append(request.POST.get('input'+str(i),'NONE'))
        job_title = request.POST.get('title','')
        job_desc = request.POST.get('desc','')
        vacancy = request.POST.get('vacancy','')
        education_years = request.POST.get('experience','')
        Job_offers = job_offers(job_title= job_title , job_desc= job_desc ,education_years=education_years,vacancy=vacancy ,company_id=resp,skills_required=int1,education =int2 )
        Job_offers.save()

        print(vacancy)


    # for item in skills:
    #     print(item[0])
    job = {'job':skills,'edu':ed}

#

    # print(skills[0][0])
    #print(request.POST)
    # skill = skills_required()
    # print(skill)




    return render(request,'joboffers.html' ,job)

def profile(request):
    return render(request,'profile.html')
