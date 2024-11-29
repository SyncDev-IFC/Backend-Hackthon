from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import Aluno, Ocorrencia

class AlunoSerializer(ModelSerializer):
    historico = SerializerMethodField()

    class Meta:
        model = Aluno
        fields = "__all__"

    def get_historico(self, obj):
        ocorrencias = Ocorrencia.objects.filter(aluno=obj)
        return [
            {
                "id": ocorrencia.id,
                "titulo": ocorrencia.titulo,
                "conteudo": ocorrencia.conteudo,
                "data_criacao": ocorrencia.data_criacao.strftime("%d/%m/%Y %H:%M"),
                "tipo": ocorrencia.get_tipo_display(), 
                "trimestre": ocorrencia.trimestre.nome if ocorrencia.trimestre else None,
            }
            for ocorrencia in ocorrencias
        ]
