from rest_framework.viewsets import ModelViewSet

from core.models import Trimestre
from core.serializers import TrimestreSerializer


class TrimestreViewSet(ModelViewSet):
    queryset = Trimestre.objects.all().order_by("id")
    serializer_class = TrimestreSerializer
