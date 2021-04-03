# 기본 
from django.shortcuts import render, redirect, get_object_or_404
# 데커레이터들
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
# 재료들 model, form
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.http import HttpResponse, HttpResponseForbidden

# R C U D 
# READ 전체조회
@require_GET
def index(request):
    articles = Article.objects.all()[::-1]
    context= {'articles':articles}
    return render(request, 'articles/index.html', context)


# READ 개별조회 => 3가지 정보를 context로 넘길거다! 
@require_GET
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 사실 이 아래줄은 DTL 단에서 for 태그로 풀거면 굳이 필요는 없다.
    comments = article.comment_set.all()
    form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'form':form,
    }
    return render(request, 'articles/detail.html', context)

# Create
@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article_pk=article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)


# Update
@login_required
@require_http_methods(['GET','POST'])
def update(request, article_pk):
    # 하나 찝어오기
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

# @login_required
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return redirect('articles:index')

@require_POST
def create_comment(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        form = CommentForm(request.POST)
        # 얘는 validation 실패시 실패한 곳까지의 폼 기입을 돌려주고, 댓글들도 전부 보이게 하기 위해서
        comments = article.comment_set.all()[::-1]

        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article.pk)

        context = {
            'article':article,
            'form':form,
            'comments':comments,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')

@require_POST
def delete_comment(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.is_authenticated: # 로그인 후 자기댓글만 지우게 한다.
        if request.user == comment.user:
            comment.delete()
            return redirect('articles:detail', article_pk=article_pk)
        return HttpResponseForbidden()
    return redirect('accounts:login')


@require_POST
def likes(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        if request.user not in article.like_users.all(): # 좋아요
            article.like_users.add(request.user)
        else:
            article.like_users.remove(request.user) # 좋아요 취소
        return redirect('articles:index')
    return redirect('accounts:login')


