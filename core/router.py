from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, TrimestreViewSet, TurmaViewSet, CursoViewSet

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'trimestres', TrimestreViewSet, basename='trimestres')
router.register(r'turmas', TurmaViewSet, basename='turmas')
router.register(r'cursos', TurmaViewSet, basename='cursos')

urlpatterns = router.urls
