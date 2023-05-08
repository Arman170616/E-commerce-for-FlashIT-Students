from django.shortcuts import render
from accounts.forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout





def register(request):
    if request.user.is_authenticated:
        return HttpResponse('You are already logged in.')
    else:
        form = RegistrationForm()
        if request.method == 'POST' or request.method == 'post':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('You have successfully registered.')

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def Customerlogin(request):
    if request.user.is_authenticated:
        return HttpResponse('You are already logged in.')
    else:
        if request.method == 'POST' or request.method == 'post':
            username = request.POST.get('username')
            password = request.POST.get('password')

            customer = authenticate(request, username=username, password=password)

            if customer is not None:
                login(request, customer)
                return HttpResponse('You have successfully logged in.')
            else:
                return HttpResponse('Invalid credentials.')

    return render(request, 'accounts/login.html')