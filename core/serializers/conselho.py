from rest_framework.serializers import ModelSerializer

from core.models import Conselho

class ConselhoSerializer(ModelSerializer):
    class Meta:
        model = Conselho
        fields = "__all__"