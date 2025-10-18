# links/views.py

from django.http import HttpResponseRedirect
import csv
from datetime import datetime
from rest_framework.views import APIView
from django.http import HttpResponse
from django.db.models import F
from rest_framework import generics
from .models import Link
from .serializers import LinkSerializer

# ... (a view LinkListCreateView que já criamos continua aqui)
class LinkListCreateView(generics.ListCreateAPIView):
    queryset = Link.objects.all().order_by('-created_at')
    serializer_class = LinkSerializer


# NOVA VIEW PARA REDIRECIONAMENTO
class LinkRedirectView(generics.RetrieveAPIView):
    """
    View que encontra um link pelo seu código, incrementa a contagem de visitas
    e redireciona para a URL original.
    """
    queryset = Link.objects.all()
    # Define que a busca do objeto será feita pelo campo 'code' e não pelo ID
    lookup_field = 'code'

    def retrieve(self, request, *args, **kwargs):
        # Pega o objeto Link usando a lógica padrão do RetrieveAPIView
        instance = self.get_object()

        # Incrementa o visit_count de forma atômica para evitar race conditions
        Link.objects.filter(pk=instance.pk).update(visit_count=F('visit_count') + 1)
        
        # Retorna uma resposta de redirecionamento
        return HttpResponseRedirect(instance.original_url)
    
# NOVA VIEW PARA DETALHAR E DELETAR
class LinkRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    """
    View para buscar os detalhes de um link (GET) ou deletá-lo (DELETE).
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    # Define que a busca do objeto será feita pelo campo 'code'
    lookup_field = 'code'


# NOVA VIEW PARA EXPORTAR CSV
class LinkExportView(APIView):
    """
    View para exportar todos os links cadastrados para um arquivo CSV.
    """
    def get(self, request, *args, **kwargs):
        # Cria uma resposta HTTP com o content-type para CSV
        response = HttpResponse(content_type='text/csv')
        
        # Define o nome do arquivo que será baixado pelo usuário
        filename = f'brevly-links-export-{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        
        # Cria um "escritor" de CSV que irá escrever na resposta HTTP
        writer = csv.writer(response)
        
        # Escreve a linha do cabeçalho no arquivo 
        writer.writerow(['Original URL', 'Shortened URL', 'Visit Count', 'Created At'])
        
        # Busca todos os links do banco de dados
        links = Link.objects.all()
        
        # Itera sobre os links e escreve uma linha para cada um
        for link in links:
            # Constrói a URL encurtada completa
            shortened_url = request.build_absolute_uri(f'/{link.code}/')
            writer.writerow([
                link.original_url, 
                shortened_url, 
                link.visit_count, 
                link.created_at.strftime("%Y-%m-%d %H:%M:%S")
            ])
            
        return response