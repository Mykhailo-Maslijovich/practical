from django.shortcuts import render, redirect
from .models import book
from .forms import BookForm



def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form':form })

def book_list(request):
    books = book.object.all()
    return render(request,'book_list.html', {'books':books})

def search_book(request):
    query = request.GET.get('q')
    books = book.objects.filter(author__icontains=query)  
    return render(request, 'search_book.html', {'books':books , 'query':query})