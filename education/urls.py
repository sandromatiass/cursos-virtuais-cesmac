from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.produto_new, name='produto_new'),
]