from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    estado = models.CharField(max_length=30)
    cpf = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
