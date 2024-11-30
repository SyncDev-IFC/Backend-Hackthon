from rest_framework.serializers import ModelSerializer, CharField
from core.models import Ocorrencia


class OcorrenciaSerializer(ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = "__all__"
