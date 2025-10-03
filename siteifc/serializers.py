from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.serializers import ModelSerializer
from .models import Eventos, Tipo_user, Turma, Grupo_estudo, Comite, Comissao, Nucleos, User, Atendimento, Vendas, Reservar, User_eventos, User_grupo, User_comite, User_comissao, User_nucleos

class EventosSerializer(ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'

class Tipo_userSerializer(ModelSerializer):
    class Meta:
        model = Tipo_user
        fields = '__all__'

class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class Grupo_estudoSerializer(ModelSerializer):
    class Meta:
        model = Grupo_estudo
        fields = '__all__'

class ComiteSerializer(ModelSerializer):
    class Meta:
        model = Comite
        fields = '__all__'

class ComissaoSerializer(ModelSerializer):
    class Meta:
        model = Comissao
        fields = '__all__'

class NucleosSerializer(ModelSerializer):
    class Meta:
        model = Nucleos
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # ou liste os campos específicos

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class AtendimentoSerializer(ModelSerializer):
    class Meta:
        model = Atendimento
        fields = '__all__'

class VendasSerializer(ModelSerializer):
    class Meta:
        model = Vendas
        fields = '__all__'

class ReservarSerializer(ModelSerializer):
    class Meta:
        model = Reservar
        fields = '__all__'

class User_eventosSerializer(ModelSerializer):
    class Meta:
        model = User_eventos
        fields = '__all__'

class User_grupoSerializer(ModelSerializer):
    class Meta:
        model = User_grupo
        fields = '__all__'

class User_comiteSerializer(ModelSerializer):
    class Meta:
        model = User_comite
        fields = '__all__'

class User_comissaoSerializer(ModelSerializer):
    class Meta:
        model = User_comissao
        fields = '__all__'

class User_nucleosSerializer(ModelSerializer):
    class Meta:
        model = User_nucleos
        fields = '__all__'


class SiteIfcAuthSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        if user.tipo_user:
            token['tipo'] = user.tipo_user.descricao
        else:
            token['tipo'] = None
        return token