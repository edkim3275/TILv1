from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    """
    POST : 실제 로그인을 진행
    GET : 로그인 페이지를 랜더
    """
    if request.method == 'POST':
        pass
    else:
        form = 
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)
