from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, AlunoViewSet

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'alunos', AlunoViewSet, basename='alunos')

urlpatterns = router.urls
