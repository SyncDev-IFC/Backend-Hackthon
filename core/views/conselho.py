from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

from core.models import Conselho, Turma, Trimestre
from core.serializers import ConselhoSerializer

class ConselhoViewSet(ModelViewSet):
    queryset = Conselho.objects.all()
    serializer_class = ConselhoSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='iniciar')
    def iniciar_conselho(self, request):
        """
        Inicia o conselho, ativando-o e configurando o campo de data_inicio e data_fim.
        O usuário deve fornecer o ID da turma, trimestre e a data de fim do conselho.
        Somente membros do grupo 'NUPE' podem iniciar o conselho.
        """
        if not request.user.groups.filter(name='NUPE').exists():
            return Response(
                {"detail": "Você não tem permissão para iniciar um conselho. Apenas membros do grupo 'NUPE' podem realizar essa ação."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        turma_id = request.data.get('turma_id')
        trimestre_id = request.data.get('trimestre_id')
        data_fim = request.data.get('data_fim')

        if not turma_id or not trimestre_id or not data_fim:
            return Response(
                {"detail": "Os campos 'turma_id', 'trimestre_id' e 'data_fim' são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data_fim = timezone.datetime.fromisoformat(data_fim)
        except ValueError:
            return Response(
                {"detail": "Formato de data_fim inválido."},
                status=status.HTTP_400_BAD_REQUEST
            )

        turma = get_object_or_404(Turma, pk=turma_id)
        trimestre = get_object_or_404(Trimestre, pk=trimestre_id)

        conselho_existente = Conselho.objects.filter(turma=turma, trimestre=trimestre).first()

        if conselho_existente:
            if conselho_existente.ativo:
                return Response(
                    {"detail": f"O conselho para a turma '{turma.nome}' e trimestre '{trimestre.name}' já está ativo."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                # Reativa o conselho existente
                conselho_existente.ativar_conselho(data_fim)
                return Response(
                    ConselhoSerializer(conselho_existente).data,
                    status=status.HTTP_200_OK
                )

        conselho = Conselho.objects.create(
            turma=turma,
            trimestre=trimestre,
            ativo=True,
            data_criacao=timezone.now(),
            data_fim=data_fim
        )

        conselho.ativar_conselho(data_fim)

        return Response(
            ConselhoSerializer(conselho).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=['post'], url_path='encerrar')
    def encerrar_conselho(self, request):
        """
        Encerra o conselho, desativando-o e configurando a data de encerramento.
        O usuário deve fornecer o ID da turma e trimestre.
        Somente membros do grupo 'NUPE' podem encerrar o conselho.
        """
        
        if not request.user.groups.filter(name='NUPE').exists():
            return Response(
                {"detail": "Você não tem permissão para encerrar um conselho. Apenas membros do grupo 'NUPE' podem realizar essa ação."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        turma_id = request.data.get('turma_id')
        trimestre_id = request.data.get('trimestre_id')

        if not turma_id or not trimestre_id:
            return Response(
                {"detail": "Os campos 'turma_id' e 'trimestre_id' são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        turma = get_object_or_404(Turma, pk=turma_id)
        trimestre = get_object_or_404(Trimestre, pk=trimestre_id)

        conselho_existente = Conselho.objects.filter(turma=turma, trimestre=trimestre, ativo=True).first()

        if not conselho_existente:
            return Response(
                {"detail": f"O conselho para a turma '{turma.nome}' e trimestre '{trimestre.name}' não está ativo."},
                status=status.HTTP_400_BAD_REQUEST
            )

        conselho_existente.ativo = False
        conselho_existente.data_encerramento = timezone.now()
        conselho_existente.save()

        return Response(
            ConselhoSerializer(conselho_existente).data,
            status=status.HTTP_200_OK
        )
