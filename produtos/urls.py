from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.cria_produto, name='cria_produto'),
    path('editar/<int:pk>/', views.edita_produto, name='edita_produto'),
    path('deleta/<int:pk>/', views.deleta_produto, name='deleta_produto'),
]