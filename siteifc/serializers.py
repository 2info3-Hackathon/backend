from rest_framework.serializers import ModelSerializer
from .models import eventos

class EventosSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'