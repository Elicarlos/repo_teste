from django.contrib import admin
from . models import Produto, Teste, Tipo

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Produto)
admin.site.register(Teste)
