from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


def register(request):
    form = UserRegisterForm()
    # return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()            
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {username}!')
            return redirect('blog-home')
        else:
            pass
            # form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
