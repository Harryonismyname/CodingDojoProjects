from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description

# Create your views here.
def index(reqest):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(reqest, 'index.html', context)

def create(request):
    errors = Course.objects.new_course_validator(request.POST)
    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/")
    else:
        new_course = Course.objects.create(name=request.POST['name'])
        new_desc = Description.objects.create(desc=request.POST['description'], course = new_course)
        return redirect('/')

def destroy_confirm(request, id):
    context={
        'course': Course.objects.get(id=id)
    }
    return render(request, 'destroy.html', context)

def remove(reqest, id):
    course_to_remove = Course.objects.get(id=id)
    course_to_remove.delete()
    return redirect('/')