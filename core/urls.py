from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('produto/', views.produto, name="produto"),
    path('lista', views.list_produto, name="lista")
    
    
]
