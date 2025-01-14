from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('account', views.about, name='about'),
    path('rating-global', views.rating, name='rating'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('create', views.create, name='create') ##(вид в поисковой строке, обращение, функция во views)
]
