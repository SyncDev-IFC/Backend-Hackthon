from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Aluno, Nota, Trimestre
from core.models import Aluno
from core.serializers import AlunoSerializer, NotaSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


    @action(detail=False, methods=['get'])
    def inferior_seis(self, request):
        alunos_com_nota_baixa = Aluno.objects.filter(
            notas__nota__lt=6
        ).distinct()

        serializer = self.get_serializer(alunos_com_nota_baixa, many=True)
        return Response(serializer.data)

