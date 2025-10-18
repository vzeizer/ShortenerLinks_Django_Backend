# brevly/urls.py
from django.contrib import admin
from django.urls import path, include
# Importe a nova view de redirecionamento
from links.views import LinkRedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Nossas rotas de API para criar e listar continuam aqui
    path('api/', include('links.urls')),
    
    # NOVA ROTA DE REDIRECIONAMENTO
    # Ela captura uma string da URL e a passa como o argumento 'code' para a view
    path('<str:code>/', LinkRedirectView.as_view(), name='link-redirect'),
]