from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm

# from django.http import HttpResponse
# Create your views here.


def home (request):
    all=Todo.objects.all()
    return render(request,'home.html',{'all':all})



def detail(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(request, 'detail.html',{'todo':todo})

def delete(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,'todo deleted succsesfully','success')
    return redirect('home')

def create(request):
    if request.method=='POST':
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            pass
    else:
        form=TodoCreateForm()

    return render(request,'create.html',{'form':form  })