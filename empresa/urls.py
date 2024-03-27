from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect, render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('login/', include('login.urls')),
    path('produtos/', include('produtos.urls')),
    path('sobre/', lambda request: render(request,'clientes/sobre.html'), name='sobre'),  
    path('', lambda request: redirect('login'), name='home'),  # Redireciona para a página de login
    path('accounts/', include('django.contrib.auth.urls')),    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
