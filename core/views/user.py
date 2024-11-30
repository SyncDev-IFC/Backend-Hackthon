from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import openpyxl
from django.http import HttpResponse
from core.models import User
from core.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Return the current authenticated user"""
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def export_users_to_excel(self, request):
        """Export users to an Excel file."""
        # Criando um novo arquivo Excel
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Usuários"

        # Adicionando cabeçalhos
        headers = ['ID', 'Nome', 'Email', 'Último Login']
        ws.append(headers)

        # Buscando os dados dos usuários
        users = User.objects.all()

        # Adicionando os dados dos usuários ao arquivo Excel
        for user in users:
            ws.append([user.id, user.name, user.email, user.last_login])

        # Preparando a resposta para baixar o arquivo
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=usuarios.xlsx'

        # Salvando o arquivo na resposta
        wb.save(response)
        return response
