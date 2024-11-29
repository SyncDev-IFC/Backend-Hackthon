from rest_framework.viewsets import ModelViewSet

from core.models import Anotacao
from core.serializers import AnotacaoSerializer

class AnotacaoViewSet(ModelViewSet):
    queryset = Anotacao.objects.all().order_by("id")
    serializer_class = AnotacaoSerializer