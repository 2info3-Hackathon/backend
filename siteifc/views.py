from rest_framework.viewsets import ModelViewSet
from .models import Eventos, Tipo_user, Grupo_estudo, Comite, Comissao, Nucleos, User, Atendimento, Vendas, Reservar, User_eventos, User_grupo, User_comite, User_comissao, User_nucleos
from .serializers import EventosSerializer, Tipo_userSerializer, Grupo_estudoSerializer, ComiteSerializer, ComissaoSerializer, NucleosSerializer, UserSerializer, AtendimentoSerializer, VendasSerializer, ReservarSerializer, User_eventosSerializer, User_grupoSerializer, User_comiteSerializer, User_comissaoSerializer, User_nucleosSerializer

class EventosViewSet(ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer

class Tipo_userViewSet(ModelViewSet):
    queryset = Tipo_user.objects.all()
    serializer_class = Tipo_userSerializer

class Grupo_estudoViewSet(ModelViewSet):
    queryset = Grupo_estudo.objects.all()
    serializer_class = Grupo_estudoSerializer

class ComiteViewSet(ModelViewSet):
    queryset = Comite.objects.all()
    serializer_class = ComiteSerializer

class ComissaoViewSet(ModelViewSet):
    queryset = Comissao.objects.all()
    serializer_class = ComissaoSerializer

class NucleosViewSet(ModelViewSet):
    queryset = Nucleos.objects.all()
    serializer_class = NucleosSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AtendimentoViewSet(ModelViewSet):
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer

class VendasViewSet(ModelViewSet):
    queryset = Vendas.objects.all()
    serializer_class = VendasSerializer

class ReservarViewSet(ModelViewSet):
    queryset = Reservar.objects.all()
    serializer_class = ReservarSerializer

class User_eventosViewSet(ModelViewSet):
    queryset = User_eventos.objects.all()
    serializer_class = User_eventosSerializer

class User_grupoViewSet(ModelViewSet):
    queryset = User_grupo.objects.all()
    serializer_class = User_grupoSerializer

class User_comiteViewSet(ModelViewSet):
    queryset = User_comite.objects.all()
    serializer_class = User_comiteSerializer

class User_comissaoViewSet(ModelViewSet):
    queryset = User_comissao.objects.all()
    serializer_class = User_comissaoSerializer

class User_nucleosViewSet(ModelViewSet):
    queryset = User_nucleos.objects.all()
    serializer_class = User_nucleosSerializer