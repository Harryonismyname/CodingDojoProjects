from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def new(request):
    return HttpResponse("placeholder to display a new for to create a new blog")

def create(request):
    return redirect("/index")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def delete(request, number):
    return redirect("/")
