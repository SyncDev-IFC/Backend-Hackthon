from rest_framework.viewsets import ModelViewSet

from core.models import Turma
from core.serializers import TurmaSerializer


class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all().order_by("id")
    serializer_class = TurmaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        for turma in queryset:
            turma.calcular_media_da_turma()
        return queryset
