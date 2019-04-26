from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kgc-home'),
    path('about/', views.about, name='about'),
    path('ministries/', views.ministries, name='ministries'),
    path('board/', views.team, name='board'),
    path('gallery/', views.gallery, name='gallery'),
    path('praise_worship/', views.praise_and_worship, name='praise_and_worship'),
    path('children_ministry/', views.children, name='children_ministry'),
    path('women_ministry/', views.women_ministry, name='women_ministry'),
    path('youths/', views.youths, name='youths'),
    path('men/', views.men_ministry, name='men'),
    path('intercessory/', views.intercessory, name='intercessory'),
    path('sermons/', views.sermons, name='sermons'),
]
