from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, TrimestreViewSet, TurmaViewSet, CursoViewSet, OcorrenciaViewSet, AlunoViewSet, DisciplinaViewSet, NotaViewSet, ConselhoViewSet, ObservacaoViewSet, AnotacaoViewSet

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'alunos', AlunoViewSet, basename='alunos')
router.register(r'disciplinas', DisciplinaViewSet, basename='disciplinas')
router.register(r'trimestres', TrimestreViewSet, basename='trimestres')
router.register(r'turmas', TurmaViewSet, basename='turmas')
router.register(r'cursos', CursoViewSet, basename='cursos')
router.register(r'notas', NotaViewSet, basename='notas')
router.register(r'ocorrencias', OcorrenciaViewSet, basename='ocorrencias')
router.register(r'conselhos', ConselhoViewSet, basename='conselhos')
router.register(r'observacoes', ObservacaoViewSet, basename='observacoes')
router.register(r'anotacoes', AnotacaoViewSet, basename='anotacoes')

urlpatterns = router.urls
