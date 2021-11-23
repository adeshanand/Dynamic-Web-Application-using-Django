from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('login')

    if request.method == 'GET':
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1!=password2:
            messages.info(request, 'Password not matching...')
            return redirect('register')
        elif User.objects.filter(username=username):
            messages.info(request, 'Username taken')
            return redirect('register')
        elif User.objects.filter(email=email):
            messages.info(request, 'Email taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login')

    if request.method == 'GET':
        return render(request, 'register.html')