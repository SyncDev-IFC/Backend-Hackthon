from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import Nota

class NotaSerializer(ModelSerializer):
    class Meta:
        model = Nota
        fields = "__all__"

class AlunoNotaSerializer(ModelSerializer):
    trimes_name = SerializerMethodField()

    class Meta:
        model = Nota
        fields = ['aluno', 'nota', 'trimes_name']
        depth = 1

    def get_trimes_name(self, obj):
        return obj.trimestre.get_name_display() if obj.trimestre else None


class NotaSmallSerializer(ModelSerializer):
    trimes_name = SerializerMethodField()
    disciplina_name = SerializerMethodField()
    class Meta:
        model = Nota
        fields = ['nota', 'trimes_name', 'disciplina_name']

    
    def get_trimes_name(self, obj):
        return obj.trimestre.get_name_display() if obj.trimestre else None
    
    def get_disciplina_name(self, obj):
        return obj.disciplina.nome if obj.disciplina else None
