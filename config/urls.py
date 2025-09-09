from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from siteifc.views import EventosViewSet, Tipo_userViewSet, Grupo_estudoViewSet, ComiteViewSet, ComissaoViewSet, NucleosViewSet, UserViewSet, AtendimentoViewSet, VendasViewSet, ReservarViewSet, User_eventosViewSet, User_grupoViewSet, User_comiteViewSet, User_comissaoViewSet, User_nucleosViewSet

router = DefaultRouter()
router.register(r'eventos', EventosViewSet)
router.register(r'tipo_usuario', Tipo_userViewSet)
router.register(r'grupo_estudo', Grupo_estudoViewSet)
router.register(r'comite', ComiteViewSet)
router.register(r'comissao', ComissaoViewSet)
router.register(r'nucleos', NucleosViewSet)
router.register(r'usuario', UserViewSet)
router.register(r'atendimento', AtendimentoViewSet)
router.register(r'vendas', VendasViewSet)
router.register(r'reservar', ReservarViewSet)
router.register(r'user_evento', User_eventosViewSet)
router.register(r'user_grupo', User_grupoViewSet)
router.register(r'user_comite', User_comiteViewSet)
router.register(r'user_comissao', User_comissaoViewSet)
router.register(r'user_nucleos', User_nucleosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
