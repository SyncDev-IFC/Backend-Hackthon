from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Ocorrencia, Trimestre
from core.serializers import OcorrenciaSerializer


class OcorrenciaViewSet(ModelViewSet):
    queryset = Ocorrencia.objects.all().order_by("data_criacao")
    serializer_class = OcorrenciaSerializer

    @action(detail=False, methods=['get'], url_path='por_trimestre/(?P<trimestre_id>\d+)')
    def por_trimestre(self, pk=None, trimestre_id=None):
        ocorrencias = Ocorrencia.objects.filter(trimestre=trimestre_id)
        
        ocorrencias_serializer = OcorrenciaSerializer(ocorrencias, many=True)

        return Response(ocorrencias_serializer.data)
        