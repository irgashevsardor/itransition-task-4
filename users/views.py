from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful.')
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    return render(request, 'users/login.html')

def panel(request):
    return render(request, 'users/panel.html')