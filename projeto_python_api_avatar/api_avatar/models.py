from django.db import models

# Create your models here.
class Personagem(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    aliados = models.CharField(max_length=200)
    inimigos = models.CharField(max_length=200)
    afiliacao = models.CharField(max_length=200)
    imagem = models.URLField(blank=True)
    
    def __str__(self):
        return list(self.id, self.nome, self.aliados, self.inimigos, self.afiliacao)