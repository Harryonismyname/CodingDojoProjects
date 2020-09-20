from django.shortcuts import render, redirect
from random import randint
# Create your views here.
def index(request):
    request.session['gold'] = request.session.get('gold', 0)
    request.session['location'] = {'farm': [10, 20], 'cave': [5,10], 'house': [2,5], 'casino':[0,50]}
    request.session['log'] = request.session.get('log', [])
    return render(request, 'index.html')

def process_money(request):
    reward = randint(request.session['location'][request.POST['location']][0], request.session['location'][request.POST['location']][1])
    if request.POST['location'] == "casino":
        give_or_take =randint(0, 100)
        if give_or_take >= 70:
            request.session['gold'] = request.session.get('gold', 0) + reward
            request.session['log'].append('Entered a casino and won {} gold!\n'.format(reward))
        elif give_or_take <= 70:
            request.session['gold'] = request.session.get('gold', 0) - reward
            request.session['log'].append("Entered a casino and lost {} gold! Next time, don't put it all in roulette\n".format(reward))
    else:
        request.session['log'].append('Earned {} gold from {}\n'.format(reward, request.POST['location']))
        request.session['gold'] = request.session.get('gold', 0) + reward
    return redirect("/")

def reset(request):
    request.session['gold'] = 0
    request.session['log'] = []
    return redirect("/")

