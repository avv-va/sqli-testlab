from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import get_hasher


def index(request):
    return render(request, 'user/index.html', {'title':'index'})
  
  
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
        else:
            messages.info(request, f'Could not create account: {form.errors.values()}')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'})


def generate_encoded_password(username, password):
    hasher = get_hasher()
    user_query = f"SELECT * FROM auth_user WHERE username = '{username}'"
    user = User.objects.raw(user_query)[0]
    user_pass_encoded = user.password
    decoded = hasher.decode(user_pass_encoded)
    input_passw_encoded = hasher.encode(password, decoded["salt"], decoded["iterations"])
    return input_passw_encoded


def _authenticate(request, username, password, sql_safe=True):
    if sql_safe:
        return authenticate(request, username = username, password = password)
    try:
        input_password_encoded = generate_encoded_password(username, password)
        auth_query = f"SELECT * FROM auth_user WHERE username = '{username}' AND password = '{input_password_encoded}'"
        user = User.objects.raw(auth_query)[0]
    except:
        user = None
    return user


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = _authenticate(request, username, password, sql_safe=False)

        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'Account does not exist or password is wrong')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})