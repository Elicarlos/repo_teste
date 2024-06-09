from django.db import models

# Create your models here.
class Tipo(models.Model):
    tipo = models.CharField(max_length=250)
    
    def __str__(self):
        return self.tipo



class Produto(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=250)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.descricao
    

class Teste(models.Model):
    teste = models.CharField(max_length=100)
    
    def __str__(self):
        return self.teste
    
    

