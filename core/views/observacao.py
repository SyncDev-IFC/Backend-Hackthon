from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Observacao
from core.serializers import ObservacaoSerializer


class ObservacaoViewSet(ModelViewSet):
    queryset = Observacao.objects.all().order_by("id")
    serializer_class = ObservacaoSerializer

    def perform_create(self, serializer):
        """
        Verifica se o usuário pertence aos grupos 'Professor' ou 'NUPE' antes de criar a observação.
        """
        if not (self.request.user.groups.filter(name='Professor').exists() or
                self.request.user.groups.filter(name='NUPE').exists()):
            raise PermissionDenied("Você não tem permissão para cadastrar uma observação.")
        
        serializer.save()

    @action(detail=False, methods=['get'], url_path='por_trimestre/(?P<trimestre_id>\d+)')
    def por_trimestre(self, pk=None, trimestre_id=None):
        observacoes = Observacao.objects.filter(trimestre=trimestre_id)
        
        observacoes_serializer = ObservacaoSerializer(observacoes, many=True)

        return Response(observacoes_serializer.data)
