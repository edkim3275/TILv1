from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

def index(request):
    """
    모든 게시물을 보여주는 탬플릿을
    
    랜더하는 함수!
    """
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    """
    게시물의 상세페이지를 랜더하는 함수!
    """
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)



def create(request):
    """
    GET : 새 글을 작성하는 탬플릿을 랜더
    POST : DB에 새 글을 생성
    """
    if request.method == 'POST':
        # 사용자로부터 받은 정보(request.POST)가 담긴 인스턴스를 생성
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # 통과하면 저장한다!
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # GET : form 클래스 사용 => 인스턴스를 생성
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def update(request, pk):
    """
    GET : 수정하는 페이지를 랜더!
    POST : DB에 수정 내용 반영!
    """
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)


# def delete 는 숙제!!! 😎