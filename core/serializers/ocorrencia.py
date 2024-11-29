from rest_framework.serializers import ModelSerializer

from core.models import Ocorrencia


class OcorrenciaSerializer(ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = "__all__"
