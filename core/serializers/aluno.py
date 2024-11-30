from core.models.observacao import Observacao
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import Aluno, Ocorrencia, Observacao

class AlunoSerializer(ModelSerializer):
    historico = SerializerMethodField()
    notas = SerializerMethodField()

    class Meta:
        model = Aluno
        fields = ["id", "nome", "foto", "email", "notas", "historico"]

    def get_historico(self, obj):
        ocorrencias = Ocorrencia.objects.filter(aluno=obj)
        observacoes = Observacao.objects.filter(aluno=obj)
    
        return {
            "ocorrencias": [
                {
                    "id": ocorrencia.id,
                    "conteudo": ocorrencia.conteudo,
                    "data_criacao": ocorrencia.data_criacao.strftime("%d/%m/%Y %H:%M"),
                    "tipo": ocorrencia.get_tipo_display(),
                }
                for ocorrencia in ocorrencias
            ],
            "observacoes": [
                {
                    "id": observacao.id,
                    "conteudo": observacao.conteudo,
                    "data_criacao": observacao.data_criacao.strftime("%d/%m/%Y %H:%M"),
                }
                for observacao in observacoes
            ],
    }



    def get_notas(self, obj):
        from core.serializers import NotaSmallSerializer
        notas = obj.notas.all()  
        return NotaSmallSerializer(notas, many=True).data
