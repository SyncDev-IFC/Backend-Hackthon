from rest_framework.viewsets import ModelViewSet

from core.models import Turma
from core.serializers import TurmaSerializer


class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all().order_by("id")
    serializer_class = TurmaSerializer

    def get_queryset(self):
        """
        Retorna o queryset da turma, que agora terá o campo `media_da_turma` calculado automaticamente.
        """
        return super().get_queryset()