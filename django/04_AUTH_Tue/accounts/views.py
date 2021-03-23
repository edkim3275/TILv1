from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()

# R => 단일 조회(/articles/pk/)
# @login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:profile', username=user.username)
    else:
        form = CustomUserChangeForm(instance=user)
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'accounts/profile.html', context)

# def index(request):
#     users = User.objects.all()
#     context = {'users': users, }
#     return render(request, 'accounts/index.html', context)


def signup(request):
    #  login 한 사용자라면,
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form, }
    
    return render(request, 'accounts/signup.html', context)


def login(request):
    # login 검증 / HTML 만드는 forms.Form 을 써서 완료
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인을 시켜야 하는데..
            auth_login(request, form.get_user())
            next_url = request.GET.get('next') # 딕셔너리.GET.get('') => value거나 None이거나
            return redirect(next_url or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {'form': form, }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')