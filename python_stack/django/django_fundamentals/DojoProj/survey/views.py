from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if request.method == "POST":
        return redirect('/results')
def results(request):
    print(request.method)
    if request.method == "POST":
        contexts ={
        'name': request.POST['name'],
        'location': request.POST['location'],
        'favlang':request.POST['favlang'],
        'comment': request.POST['comment']
        }
        return render(request, 'results.html', contexts)
    if request.method == "GET":
        redirect("/")