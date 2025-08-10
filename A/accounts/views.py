from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

# Create your views here.



def user_register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user()
    else:
        form=UserRegistrationForm()
    return render(request, 'register.html', {'form':form})