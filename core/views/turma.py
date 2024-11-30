from rest_framework.viewsets import ModelViewSet
from core.models import Turma
from core.serializers import TurmaSerializer

class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all().order_by("id")
    serializer_class = TurmaSerializer

    def get_queryset(self):
        """
        Retorna o queryset das turmas. Usuários superusuários e administradores
        veem todas as turmas, enquanto professores veem as turmas de acordo com 
        as disciplinas em que lecionam.
        """
        usuario = self.request.user
        
        if usuario.is_superuser:
            return Turma.objects.all()

        if usuario.groups.filter(name="NUPE").exists():
            return Turma.objects.all()

        if usuario.groups.filter(name="Professor").exists():
            return Turma.objects.filter(disciplinas__professor=usuario)

        return Turma.objects.none()
