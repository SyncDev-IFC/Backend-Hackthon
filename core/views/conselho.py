from rest_framework.viewsets import ModelViewSet

from core.models import Conselho
from core.serializers import ConselhoSerializer

class ConselhoViewSet(ModelViewSet):
    queryset = Conselho.objects.all()
    serializer_class = ConselhoSerializer