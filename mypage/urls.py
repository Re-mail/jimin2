from django.urls import path
from django.conf.urls import include
from . import views

appname = 'mypage'
urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('new_address/', views.new_address, name='new_address'),
    path('polls/',views.polls, name='polls'),
    path('polls/<int:qid>',views.detail, name='detail'),
    path('polls/vote/',views.vote, name='vote'),
]