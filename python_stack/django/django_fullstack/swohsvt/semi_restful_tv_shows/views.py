from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
    return redirect("/shows")

def shows(request):
    context={
        'all_shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    Show.objects.create(title=request.POST['Title'], network=request.POST['Network'], release_date=request.POST['Release Date'], description=request.POST['Description'])
    return redirect('/shows')

def about(request, id):
    context={'id': id, 'show':Show.objects.get(id=id)}
    return render(request, 'about.html', context)

def edit(request,id):
    context = {'id': id, 'show':Show.objects.get(id=id)}
    print(context['show'].release_date)
    release_date = context['show'].release_date
    context['release_date'] = str(release_date)
    return render(request, 'edit.html', context)

def update(request, id):
    updated_object= Show.objects.get(id=id)
    updated_object.title=request.POST['Title']
    updated_object.network=request.POST['Network']
    updated_object.release_date=request.POST['Release Date']
    updated_object.description=request.POST['Description']
    updated_object.save()
    return redirect('/shows')

def destroy(request, id):
    deleted_object= Show.objects.get(id=id)
    deleted_object.delete()
    return redirect('/shows')
