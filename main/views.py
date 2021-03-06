from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, bookShop


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def books(request):
    book_shop = bookShop.objects.all()
    return render(request, "books.html", {"book_shop": book_shop})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_books(request):
    form = request.POST
    title = form["title_text"]
    subtitle = form["subtitle_text"]
    description = form["description_text"]
    price = form["price_text"]
    genre = form["genre_text"]
    author = form["author_text"]
    year = form["year_text"]
    book = bookShop(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(books)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def marked_book(request, id):
    book = bookShop.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(books)

def unmarked_book(request, id):
    book = bookShop.objects.get(id=id)
    book.is_favorite = False
    book.save()
    return redirect(books)

def delete_book(request, id):
    book = bookShop.objects.get(id=id)
    book.delete()
    return redirect(books)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)
