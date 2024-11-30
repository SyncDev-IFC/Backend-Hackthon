from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.models import Turma, Aluno, Curso
from core.serializers import AlunoSerializer


class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome', 'image', 'cor']  # Include all fields you want to display

class TurmaSerializer(ModelSerializer):
    alunos = SerializerMethodField()
    curso = CursoSerializer() 

    class Meta:
    
        model = Turma
        fields = "__all__"


    def get_alunos(self, obj):
        alunos = Aluno.objects.filter(turma=obj)
        return AlunoSerializer(alunos, many=True).data

