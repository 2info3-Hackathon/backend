from rest_framework.viewsets import ModelViewSet
from .models import Eventos
from .serializers import EventosSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer