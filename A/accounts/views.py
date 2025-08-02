from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.



def user_register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            pass
    else:
        form=UserRegistrationForm()
    return render(request, 'register.html', {'form':form})