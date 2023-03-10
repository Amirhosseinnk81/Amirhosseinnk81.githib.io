from distutils.log import INFO
from django.shortcuts import render
from contact_app.models import message , info
from resume_app.models import resume

def home(request):
    if request.method == "post":
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        body = request.POST.get('body')
        message.objects.create(name=name, email=email,sub=sub, body=body)
        print("hello")

    infor = info.objects.all().last()
    resumes = resume.objects.all()
    return render(request, "index.html",context={'resumes' : resumes,'infor' : infor})