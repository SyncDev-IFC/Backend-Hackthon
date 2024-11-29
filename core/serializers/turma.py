from rest_framework.serializers import ModelSerializer

from core.models import Turma


class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = "__all__"
