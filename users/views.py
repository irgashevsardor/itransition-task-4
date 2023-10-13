from django.shortcuts import render
from .forms import RegisterUserForm

# Create your views here.


def register_user(request):
    form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    return render(request, 'users/login.html')