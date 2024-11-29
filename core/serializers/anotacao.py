from rest_framework.serializers import ModelSerializer
from core.models import Anotacao

class AnotacaoSerializer(ModelSerializer):
    class Meta:
        model = Anotacao
        fields = "__all__"