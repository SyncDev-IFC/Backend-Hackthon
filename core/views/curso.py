from rest_framework.viewsets import ModelViewSet

from core.models import Curso
from core.serializers import CursoSerializer


class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer
