from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, AlunoViewSet, DisciplinaViewSet

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'alunos', AlunoViewSet, basename='alunos')
router.register(r'disciplinas', DisciplinaViewSet, basename='disciplinas')

urlpatterns = router.urls
