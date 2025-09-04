from django.contrib import admin
from .models import Eventos, Tipo_user, Grupo_estudo, Comite, Comissao, Nucleos, User, Atendimento, Vendas, Reservar, User_eventos, User_grupo, User_comite, User_comissao, User_nucleos

# Register your models here.

admin.site.register(Eventos)
admin.site.register(Tipo_user)
admin.site.register(Grupo_estudo)
admin.site.register(Comite)
admin.site.register(Comissao)
admin.site.register(Nucleos)
admin.site.register(User)
admin.site.register(Atendimento)
admin.site.register(Vendas)
admin.site.register(Reservar)
admin.site.register(User_eventos)
admin.site.register(User_grupo)
admin.site.register(User_comite)
admin.site.register(User_comissao)
admin.site.register(User_nucleos)