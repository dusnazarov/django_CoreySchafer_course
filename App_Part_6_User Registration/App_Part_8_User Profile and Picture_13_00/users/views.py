from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required



def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
        else:
            form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})            


@login_required
def profile(request):
    return render(request, 'users/profile.html')
