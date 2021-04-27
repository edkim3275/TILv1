from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # GET/POST => /api/articles/
    path('articles/', views.article_list_or_create),
    
    # GET/PUT/DELETE => /api/articles/1/
    path('articles/<int:article_pk>/', views.article_detail_or_update_or_delete),


    # POST => /api/articles/<pk>/comments/  =>  댓글 생성
    path('articles/<int:article_pk>/comments/', views.create_comment),

    # PUT/DELETE => /api/articles/<pk>/comments/<pk>/  => 단일 댓글 수정/삭제
    path('articles/<int:article_pk>/comments/<int:comment_pk>/', views.update_or_delete_comment),

]
