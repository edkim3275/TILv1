from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm

# DB에 유저 세션 생성(CREATE)
def login(request):
    """
    POST : 실제 로그인을 진행
    GET : 로그인 페이지를 랜더
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())

            # next 파라미터를 여기서 활용!
            # A or B
            # A : request.GET.get('next')가 존재한다면 B를 확인하지 않고 A를 사용
            # A가 존재하지 않는다면 B를 사용
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        # form 인스턴스 : Form Class를 직접 만들지 않음
        form = AuthenticationForm(request)
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


# DB 유저 세션 삭제(DELETE)
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

# DB 유저 정보 생성(CREATE)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 알잘딱깔센 => 로그인(받아온 유저로)
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html',context)

# DB 유저 정보 수정(UPDATE)
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 유저 정보수정이기 때문에 이전 내용이 필요
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

# DB 유저 정보 삭제
@require_POST
def delete(request):
    # 로그인 한 사람이면 삭제
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')

# DB 비밀번호 수정(UPDATE)
def change_password(request):
    if request.method == 'POST':
        pass
    else:
        form = PasswordChangeForm(request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/update.html', context)