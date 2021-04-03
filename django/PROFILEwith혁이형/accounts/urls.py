from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password/', views.change_password, name='change_password'),
    # update는 왜 앞에 pk를 받지 않는가?
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
    # 원래 str 이니까 굳이 안붙여도 됨.
    path('<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
