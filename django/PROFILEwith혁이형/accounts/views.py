# 기본세팅
from django.shortcuts import render, redirect, get_object_or_404
# 데커레이터들
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
# 재료들 model, form => 모델을 안쓰는 이유는 3군데서 자가조달이 가능하기 때문.
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    # UserCreationForm,
    # UserChangeForm,
)
from .forms import CustomUserChangeForm, CustomUserCreationForm
# 로그인 로그아웃, 패스워드와 관련된 것
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
# 유저리스트를 출력해라! 라고하면 유저 객체를 가져와야해서. 그리고 프로필에서 User 가 필요해서 여기 import 해야돼.
from django.contrib.auth import get_user_model


# 세선 테이블의 생성과 삭제
# login_required 쓰면 사이트 자체가 조짐.
@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # form.save()
            auth_login(request, form.get_user())  # 유저 자가조달 1 번째
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm(request)
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 유저 자가조달 2번째
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)


@login_required
@require_http_methods(['GET','POST'])
def edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)  # 유저 자가조달 3번째
        if form.is_valid():
            form.save()
            return redirect('articles:index')
            # return redirect('accounts:profile', form.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {'form':form}

    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # 여기가 왜 form user 일까.. request.user 해도 되나?
            return redirect('articles:index')

    else:
        form = PasswordChangeForm(request.user)
    
    context = {'form':form}
    return render(request, 'accounts/change_password.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {'person':person}
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        me = request.user
        you = get_object_or_404(get_user_model(), pk=user_pk)
        if me != you:
            if you.fans.filter(pk=me.pk).exists(): # 팔로우 취소!
                me.stars.remove(you) 
                # you.fans.remove(me) 이렇게 적으면 내가 팔로위 취소하는게 아니라 쟤가 나를 remove 하는 느낌.
            else:
                me.stars.add(you)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
        
