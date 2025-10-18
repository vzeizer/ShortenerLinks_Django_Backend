# links/urls.py
from django.urls import path
# Importe a nova view unificada
from .views import LinkListCreateView, LinkRetrieveDestroyView, LinkExportView  # NOVA IMPORTAÇÃO

urlpatterns = [
    # Esta rota agora aponta para a view que lida com GET e POST
    path('links/', LinkListCreateView.as_view(), name='link-list-create'),
    # NOVA ROTA para detalhar (GET) e deletar (DELETE) um link específico
    path('links/export/', LinkExportView.as_view(), name='link-export'), # NOVA ROTA
    path('links/<str:code>/', LinkRetrieveDestroyView.as_view(), name='link-retrieve-destroy'),
]