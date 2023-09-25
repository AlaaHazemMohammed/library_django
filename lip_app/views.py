from django.shortcuts import render ,redirect ,get_object_or_404
# from flask import Flask, render_template, request,
from .models import *
from .forms import *
# Create your views here.



def index(request):
    if request.method == 'POST':
       add_book = addbook(request.POST , request.FILES)
       if add_book.is_valid():
          add_book.save()

       add_category = catrgoryadd(request.POST)
       if add_category.is_valid():        
           add_category.save()


         #return render (request,'pages/index.html' ,context)
          
    context={
    'category':category.objects.all(),
    'book':Book.objects.all(),
    'form': addbook(),
    'cform':catrgoryadd(),
    'allbook':Book.objects.filter(active=True).count(),
    'booksold':Book.objects.filter(status='sold').count(),
    'bookrental':Book.objects.filter(status='rental').count(),
    'bookvalid':Book.objects.filter(status='availble').count(),
    }
    return render (request,'pages/index.html' ,context)

def books(request):

    if request.method == 'POST':
       add_book = addbook(request.POST , request.FILES)
       if add_book.is_valid():
          add_book.save()

       add_category = catrgoryadd(request.POST)
       if add_category.is_valid():        
           add_category.save()


    search = Book.objects.all()
    title= None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title :
            search = search.filter(title__icontains=title)


    context={
    'category':category.objects.all(),
    'book':search,
    'form': addbook(),
    'cform':catrgoryadd(),
    }
    return render(request,'pages/books.html',context)


def update(request ,id):
    bookid = Book.objects.get(id=id)
    if request.method=='POST':
        bookupdate = addbook(request.POST , request.FILES , instance=bookid )
        if bookupdate.is_valid():
            bookupdate.save()
            return redirect('/')
    else:
        bookupdate = addbook(instance=bookid)  

    context={
        'form':bookupdate
    }
    return render(request,'pages/update.html',context)



def delete(request ,id):
    # bookiddelete = Book.objects.get(id=id)
    bookiddelete = get_object_or_404(Book ,id=id)
    if request.method=='POST':
       bookiddelete.delete()
       return redirect('/')    
    return render(request,'pages/delete.html')
