from core.serializers.disciplina import DisciplinaSerializer
from rest_framework.viewsets import ModelViewSet

from core.models import Disciplina
from core.serializers import DisciplinaSerializer

class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    