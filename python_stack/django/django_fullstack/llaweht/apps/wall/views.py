from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment

# Create your views here.
def index(request):
    if 'current_user' not in request.session:
        messages.error(request, 'You must be logged in or register!')
        return redirect('/')
    else:
        context={
            'user': User.objects.get(id=request.session['current_user']),
            'posts': Message.objects.all(),
            'comments': Comment.objects.all()
        }
        return render(request, 'wall/index.html', context)
    
def make_post(request):
    if 'current_user' not in request.session:
        messages.error(request, 'You must be logged in or register!')
        return redirect('/')
    if request.method == 'POST':
        current_user = User.objects.get(id=request.session['current_user'])
        new_post = Message.objects.create(user=current_user, message=request.POST['textbox'])
        return redirect('/user/home')
    return redirect('/user/home')

def make_comment(request):
    if 'current_user' not in request.session:
        messages.error(request, 'You must be logged in or register!')
        return redirect('/')
    if request.method == 'POST':
        current_user = User.objects.get(id=request.session['current_user'])
        current_message = Message.objects.get(id=request.POST['post_id'])
        new_comment = Comment.objects.create(user=current_user, message=current_message, comment=request.POST['comment'])
        return redirect('/user/home')
    else:
        print("HAHA YOU DIED!")
        return redirect('/user/home')
