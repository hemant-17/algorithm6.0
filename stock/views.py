from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . models import *
from lock.models import *

# Create your views here.

# def home(request):
#     return render(request,'home.html')
# Create your views here.
# def StudentHome(request):
#     alla = User.objects.get(username='soham')
#     print(alla)
#     print(alla.skills)
#     # alla.skills=''
#     # alla.save()
#     print(alla.skills)
#     return HttpResponse("done")

# def homePage(request):
#     print('hi')
#     return render(request,'student/home.html')
def courses(request):
    return render(request,'courses.html')

def Profile(request,user):
    print(request.user)
    print("hello")
    profiles = StudentUser.objects.get(username=user)
    print(profiles)
    profiles ={'profile': profiles,'skills':SKILLS_CHOICES}
    # if request.method=='POST':
    #     print(request.FILES)
    #     form = StudentUser(request.POST, request.FILES)
    #     form.save()
    return render(request,'profile.html',profiles)

def jobview(request,Comp,jobtitle,username1):
    compa= company.objects.get(company_name=Comp)
    print(compa)
    job = job_offers.objects.get(job_title=jobtitle)
    job1 =str(job.skills_required)
    job2 = job1.split(',')
    print(len(job2))
    # print(count(job1))
    use =StudentUser.objects.get(username=username1)
    use1 =str(use.skills)
    use2= use1.split(',')
    print(len(use2))
    param={'company':compa,'job':job,'user':len(use2),'req':len(job2)}
    return render(request,'view_job.html',param)

def contact(request):
    return render(request,'contactus.html')
def about(request):
    return render(request,'aboutus.html')

def jobs(request):
    jobs=job_offers.objects.all()
    job={'job':jobs}
    return render(request,"jobs.html",job)
def home(request):
    return render(request,'home.html')

def sign(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        username1=request.POST.get('username','')
        email1=request.POST.get('email','')
        password1= request.POST.get('password1','')
        password2= request.POST.get('password2','')


        if password1==password2:
            if User.objects.filter(username=username1).exists():
                messages.info(request, 'USERNAME already registered ')
                return redirect('/stock/sign/')

            else:
                user = User.objects.create_user( first_name=first_name,last_name=last_name, username=username1, email=email1, password=password1 )
                user.save()
                newuser=StudentUser()
                newuser.username=username1
                newuser.email=email1
                newuser.save()
                return redirect('/stock/login/')

        else:
            messages.info(request, 'Confirm password did not match ')
            return redirect('/stock/sign/')

    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        User=auth.authenticate(username=username,password=password)

        if User is not None:
            auth.login(request,User)
            username=request.user.username
            return redirect("/stock")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login/')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)

    return redirect("/")

# def profile(request):
#     return render(request,'profile.html')

# def courses(request):
#     return render(request,'courses.html')

def course1(request):
    return render(request,'nptel.html')

def projects(request):
    return render(request,'project.html')

def ui(request):
    return render(request,'ui.html')

def quiz(request):
    return render(request,'quiz.html')


def apply(request,email1,jobtitle1,username2):
    appl = applicants()
    appl.email=email1
    appl.username=username2
    appl.title=jobtitle1
    appl.save()
    print("done")
    return redirect('/students/jobs/')

def display(request):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',
                  {'post':post})
