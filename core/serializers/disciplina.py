from rest_framework.serializers import ModelSerializer
from core.models import Disciplina

class DisciplinaSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = "__all__"