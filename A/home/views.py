from django.shortcuts import render
from .models import Todo
# from django.http import HttpResponse
# Create your views here.


def home (request):
    all=Todo.objects.all()
    return render(request,'home.html',{'all':all})

def say_hello(request):
    # person ={'name':'zahra'}
    return render(request,'hello.html',{'name':'adminn'})


def detail(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(request,'detail.html',{'todo':todo})