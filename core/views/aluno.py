from rest_framework.viewsets import ModelViewSet

from core.models import Aluno
from core.serializers import AlunoSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer