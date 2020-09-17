from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
def index (request):
    request.session['rando_word'] = get_random_string(length=14)
    request.session['attempt_num']=request.session.get('attempt_num', 0) + 1    
    return render(request, 'index.html')