from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from http.client import HTTPResponse
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs':jobs})

def job_page(request, myid):
    job = Job.objects.get(id=myid)
    return render(request, 'job_page.html', {'job':job})

def search(request):
    if request.method=='POST':
        searched = request.POST.get('searched')
        jobs = Job.objects.all()
        if searched:
            jobs1 = jobs.filter(title__icontains=searched)
            jobs2 = jobs.filter(company__icontains=searched)
            jobs3 = jobs.filter(location__icontains=searched)
        jobs = jobs1 | jobs2 | jobs3
        return render(request, 'home.html', {'jobs':jobs})
    else:
        return redirect('home')

def handle_login(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username = loginusername, password = loginpass)
        if user is not None:
            if user.is_superuser:
                    login(request, user)
                    return redirect("add_job")
        else:
            return redirect('home')
    return HTTPResponse('404 - Not Found')

@login_required
def add_job(request):
    return render(request, 'add_details.html')

def add_job_submit(request):
    if request.method=='POST':
        company=request.POST['company']
        title = request.POST['job_title']
        location = request.POST['location']
        description = request.POST['description']
        url = request.POST['url']
        logo = request.FILES['logo']

        ext = logo.name.split('.')[-1]
        new_name = company+title+'.'+ext
        logo.name = new_name

        job = Job.objects.create(company=company, title=title, location=location, description=description, url = url, logo = logo)
        job.save()
        return redirect('dashboard')
    return redirect('dashboard')

def dashboard(request):
    jobs = Job.objects.all().order_by('-company')
    return render(request, 'dashboard.html', {'jobs':jobs})

def edit_job(request, myid):
    job = Job.objects.get(id=myid)
    return render(request, 'edit_job.html', {'job':job})

def edit_job_submit(request, myid):
    job = Job.objects.get(id=myid)
    if request.method == "POST":
        company=request.POST['company']
        title = request.POST['job_title']
        location = request.POST['location']
        description = request.POST['description']
        url = request.POST['url']
        logo = request.FILES['logo']

        job.title = title
        job.company = company
        job.location = location
        job.description = description
        job.url = url
        
        if logo:
            ext = logo.name.split('.')[-1]
            new_name = company+title+'.'+ext
            logo.name= new_name
            job.logo = logo
        
        job.save()

        return redirect('dashboard')
    return redirect('dashboard')

def job_delete(request, myid):
    job = Job.objects.get(id = myid)
    job.delete()
    return redirect('dashboard')

def handle_logout(request):
    logout(request)
    return redirect('home')