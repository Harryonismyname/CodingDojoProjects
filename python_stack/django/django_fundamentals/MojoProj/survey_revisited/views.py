from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['favlang'] = request.POST['favlang']
        request.session['comment'] = request.POST['comment']
        return redirect('/results')
def results(request):
    print(request.method)
    if request.method == "POST":
        return redirect("/")
    if request.method == "GET":
        return render(request, 'results.html')