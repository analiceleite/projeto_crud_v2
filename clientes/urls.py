from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('novo/', views.cria_cliente, name='cria_cliente'),
    path('editar/<int:pk>/', views.edita_cliente, name='edita_cliente'),
    path('deletar/<int:pk>/', views.deleta_cliente, name='deleta_cliente'),
]