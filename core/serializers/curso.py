from rest_framework.serializers import ModelSerializer

from core.models import Curso


class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"
