from django.shortcuts import render, redirect
from django.contrib import messages
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
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['Title'], network=request.POST['Network'], release_date=request.POST['Release Date'], description=request.POST['Description'])
        return redirect('/shows')

def about(request, id):
    context={'id': id, 'show':Show.objects.get(id=id)}
    return render(request, 'about.html', context)

def edit(request,id):
    context = {'id': id, 'show':Show.objects.get(id=id)}
    release_date = context['show'].release_date
    context['release_date'] = str(release_date)
    return render(request, 'edit.html', context)

def update(request, id):
    errors = Show.objects.basic_validator(request.POST, Show.objects.get(id=id))
    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/shows/{id}/edit')
    else:
        updated_object= Show.objects.get(id=id)
        updated_object.title=request.POST['Title']
        updated_object.network=request.POST['Network']
        updated_object.release_date=request.POST['Release Date']
        updated_object.description=request.POST['Description']
        updated_object.save()
        return redirect(f'/shows/{id}')

def destroy(request, id):
    deleted_object= Show.objects.get(id=id)
    deleted_object.delete()
    return redirect('/shows')
