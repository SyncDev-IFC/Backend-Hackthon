from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Aluno, Nota, Ocorrencia, Trimestre
from core.serializers import AlunoSerializer


class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    @action(detail=False, methods=["get"])
    def inferior_seis(self, request):
        alunos_com_nota_baixa = Aluno.objects.filter(notas__nota__lt=6).distinct()

        serializer = self.get_serializer(alunos_com_nota_baixa, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def com_ocorrencias(self, request):
        alunos_com_ocorrencias = Aluno.objects.filter(ocorrencias__isnull=False).distinct()

        serializer = self.get_serializer(alunos_com_ocorrencias, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def filtrar_por_nome(self, request):
        nome = request.query_params.get("nome", None)

        if nome:
            alunos_filtrados = Aluno.objects.filter(nome__icontains=nome)
        else:
            alunos_filtrados = Aluno.objects.all()

        serializer = AlunoSerializer(alunos_filtrados, many=True)
        return Response(serializer.data)
