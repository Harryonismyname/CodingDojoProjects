from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index (request): 
    return render(request, 'index.html')

def submit(request):
    request.session['rando_word'] = get_random_string(length=14)
    request.session['attempt_num']=request.session.get('attempt_num', 0) + 1
    return redirect("/")

def reset(request):
    request.session['attempt_num'] = 0
    return redirect("/")
