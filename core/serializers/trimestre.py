from rest_framework.serializers import ModelSerializer

from core.models import Trimestre


class TrimestreSerializer(ModelSerializer):
    class Meta:
        model = Trimestre
        fields = "__all__"
