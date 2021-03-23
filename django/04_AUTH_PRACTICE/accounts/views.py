from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login # 로그인
from django.contrib.auth import logout as auth_logout # 로그아웃
from django.contrib.auth.forms import AuthenticationForm# 로그인
from django.contrib.auth import get_user_model # 모델 가져올 때
from .forms import CustomUserCreationForm # 회원가입
from django.contrib.auth.decorators import login_required # 로그인 데코
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

User = get_user_model()


def index(request):
    users = User.objects.all()
    context = {'users': users,}
    return render(request, 'accounts/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)


# session class 안에서의 Create
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm(request)
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)


# session class 안에서의 DELETE
@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')


def update(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm(instance=user)
        context = {'form': form}
        return render(request, 'accounts/update.html', context)


def delete(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        user.delete()
        auth_logout(request)
        return redirect('accounts:index')


def change_pw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/change_pw.html', context)