from rest_framework.viewsets import ModelViewSet

from core.models import Disciplina
from core.serializers import AlunoSerializer

class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = AlunoSerializer
    