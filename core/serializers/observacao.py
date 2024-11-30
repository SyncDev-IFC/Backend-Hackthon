from rest_framework.serializers import ModelSerializer

from core.models import Observacao

class ObservacaoSerializer(ModelSerializer):
    class Meta:
        model = Observacao
        fields = "__all__"