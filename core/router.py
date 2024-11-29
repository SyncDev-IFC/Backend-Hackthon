from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, TrimestreViewSet, TurmaViewSet

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'trimestres', TrimestreViewSet, basename='trimestres')
router.register(r'turmas', TurmaViewSet, basename='turnas')

urlpatterns = router.urls
