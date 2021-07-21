from django.contrib import admin
from .models import Categoria,Contato

class ContatoAdmin (admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','email','categoria', 'mostrar')
    list_display_links=('nome','sobrenome')
    list_editable = ('telefone','mostrar') # Torna os campos editáveis no admin sem precisar acessar o contato.
    list_per_page = 10
    search_fields = ('nome','sobrenome','telefone')

admin.site.register(Categoria)
admin.site.register(Contato,ContatoAdmin)