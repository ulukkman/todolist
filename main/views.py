from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def mybooks(request):
    book_shop = BookShop.objects.all()
    return render(request, "books.html", {"book_shop:" book_shop})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

