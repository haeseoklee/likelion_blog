from django.shortcuts import render
from django.shortcuts import redirect
# 로그인에 필요한 파일
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('blog')
        else:
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('blog')
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            password = request.POST['password1']
            if not User.objects.filter(username__contains = username):
                user = User.objects.create_user(username = username, password = password)
                auth.login(request, user)
                return redirect('blog')
            else:
                return redirect('signup')
    return render(request, 'accounts/signup.html')