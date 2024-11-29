from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from core.models import Anotacao, Conselho
from core.serializers import AnotacaoSerializer

class AnotacaoViewSet(ModelViewSet):
    queryset = Anotacao.objects.all().order_by("id")
    serializer_class = AnotacaoSerializer

    def perform_create(self, serializer):
        """
        Valida se o Conselho está ativo e se o usuário pertence ao grupo 'NUPE'.
        """
        if not self.request.user.groups.filter(name='NUPE').exists():
            raise PermissionDenied("Você não tem permissão para criar anotações.")

        conselho = serializer.validated_data.get('conselho')

        if not conselho.ativo:
            raise PermissionDenied("Não é possível criar uma anotação, pois o conselho não está ativo.")

        serializer.save()
