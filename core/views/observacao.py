from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Observacao
from core.serializers import ObservacaoSerializer

class ObservacaoViewSet(ModelViewSet):
    queryset = Observacao.objects.all().order_by("id")
    serializer_class = ObservacaoSerializer



        