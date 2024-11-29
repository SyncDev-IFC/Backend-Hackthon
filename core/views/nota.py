from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import Nota, Trimestre
from core.serializers import NotaSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    @action(detail=False, methods=['get'])
    def notas_por_trimestre(self, request):
        trimestre_id = request.query_params.get('trimestre', None)

        if not trimestre_id:
            return Response({"detail": "Trimestre não fornecido."}, status=400)

        try:
            trimestre = Trimestre.objects.get(id=trimestre_id)
        except Trimestre.DoesNotExist:
            return Response({"detail": "Trimestre não encontrado."}, status=404)

        notas_no_trimestre = Nota.objects.filter(trimestre=trimestre)

        notas_serializer = NotaSerializer(notas_no_trimestre, many=True)

        return Response(notas_serializer.data)
