from core.models.observacao import Observacao
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import Aluno, Ocorrencia, Observacao
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer
class AlunoSerializer(ModelSerializer):
    historico = SerializerMethodField()
    notas = SerializerMethodField()
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=False, 
    )
    foto = ImageSerializer(
        required=False,
        read_only=True
    )

    class Meta:
        model = Aluno
        fields = ["id", "nome", "foto", "foto_attachment_key", "email", "notas", "historico"]

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

