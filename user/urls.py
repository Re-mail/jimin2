from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),  # 직접 작성한 login 함수와 매핑
    path('logout/', views.logout, name='logout'),  # 직접 작성한 logout 함수와 매핑
    path('about/', views.about, name='about'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name= 'logout'), #수정
]