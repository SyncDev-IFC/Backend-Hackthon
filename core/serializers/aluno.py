from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import Aluno, Ocorrencia

class AlunoSerializer(ModelSerializer):
    historico = SerializerMethodField()
    notas = SerializerMethodField()

    class Meta:
        model = Aluno
        fields = "__all__"

    def get_historico(self, obj):
        # Obtém as ocorrências relacionadas ao aluno
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

    def get_notas(self, obj):
        from core.serializers import AlunoNotaSerializer
        notas = obj.notas.all()  
        return AlunoNotaSerializer(notas, many=True).data
