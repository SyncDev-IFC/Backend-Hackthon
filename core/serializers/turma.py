from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.models import Turma, Aluno
from core.serializers import AlunoSerializer

class TurmaSerializer(ModelSerializer):
    alunos = SerializerMethodField()
    # media = SerializerMethodField()

    class Meta:
        model = Turma
        fields = "__all__"
        depth = 1


    def get_alunos(self, obj):
        alunos = Aluno.objects.filter(turma=obj)
        return AlunoSerializer(alunos, many=True).data

    # def get_media(self, obj):
    #     return obj.calcular_media()