from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        # Define os campos que serão retornados na resposta
        fields = ['id', 'code', 'original_url', 'visit_count', 'created_at']
        # O 'code' não precisa ser enviado na requisição, pois é gerado automaticamente
        read_only_fields = ['id', 'code', 'visit_count', 'created_at']