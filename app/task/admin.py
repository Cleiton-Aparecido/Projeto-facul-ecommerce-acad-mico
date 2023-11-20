from django.contrib import admin

# Register your models here.
from task.models import *

# Register your models here.
admin.site.register(Instituicoes)
admin.site.register(Itens)
admin.site.register(Pagamentos)
admin.site.register(Compras)
admin.site.register(Carrinhos)
admin.site.register(Vendas)
admin.site.register(FormasDePagamentos)
admin.site.register(Imagens)
admin.site.register(Comentarios)
admin.site.register(Curtidas)