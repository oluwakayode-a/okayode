from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>', views.category, name='category'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name="about"),
    path('search/', views.search, name='search'),
    path('post/<slug:slug>', views.post, name='post'),   
]