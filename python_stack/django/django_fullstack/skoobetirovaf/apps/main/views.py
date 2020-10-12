from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book

def error_report(request, errors):
    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request, v)
        return True
    else:
        return False

# Create your views here.
def index(request):
    if 'current_user' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['current_user']),
            'all_books': Book.objects.all()
        }
        return render(request, 'main/index.html', context)

def create(request):
    if 'current_user' not in request.session:
        return redirect('/')
    elif request.method =="POST":
        errors= Book.objects.book_validator(request.POST)
        if error_report(request, errors):
            return redirect('/user/books')
        else:
            user = User.objects.get(id=request.session['current_user'])
            new_book = Book.objects.create(title=request.POST['title'], desc=request.POST['description'], uploaded_by=user)
            new_book.users_who_like.add(user)
            return redirect('/user/books')
    return redirect('/user/books')

def favorite(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    else:
        if request.method == 'POST':
            user = User.objects.get(id=request.session['current_user'])
            book = Book.objects.get(id=id)
            book.users_who_like.add(user)
            return redirect(f'/user/books/{id}')
        else:
            return redirect('/user/books')

def view(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['current_user']),
            'book': Book.objects.get(id=id)
        }
        return render(request, 'main/view.html', context)
    return redirect('/user/books')

def update(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    else:
        if request.method == 'POST':
            errors= Book.objects.book_validator(request.POST)
            if error_report(request, errors):
                return redirect(f'/user/books/{id}')
            else:
                book = Book.objects.get(id=id)
                user= User.objects.get(id=request.session['current_user'])
                if user == book.uploaded_by:
                    print("congrats! you got here!")
                    book.title= request.POST['title']
                    book.desc = request.POST['description']
                    book.save()
                    return redirect(f'/user/books/{id}')
                else:
                    return redirect(f'/user/books/{id}')
        else:
            return redirect(f'/user/books/{id}')

def delete(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    else:
        if request.method == 'POST':
            book = Book.objects.get(id=id)
            user= User.objects.get(id=request.session['current_user'])
            if user == book.uploaded_by:
                book.delete()
                return redirect('/user/books')
            else:
                return redirect(f'/user/books/{id}')
        else:
            return redirect(f'/user/books/{id}')

def unlike(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    else:
        user= User.objects.get(id=request.session['current_user'])
        book = Book.objects.get(id=id)
        user.liked_books.remove(book)
        return redirect(f'/user/books/{id}')

