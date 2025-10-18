# links/models.py
from django.db import models
import random
import string

def generate_unique_code():
    # Lógica simples para gerar um código, pode ser aprimorada
    length = 8
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not Link.objects.filter(code=code).exists():
            return code

class Link(models.Model):
    # O Django cria um `id` autoincremento por padrão
    code = models.CharField(max_length=15, unique=True, default=generate_unique_code)
    original_url = models.URLField()
    visit_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} -> {self.original_url}"