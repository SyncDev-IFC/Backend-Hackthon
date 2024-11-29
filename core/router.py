from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, TrimestreViewSet

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'trimestres', TrimestreViewSet, basename='trimestres')

urlpatterns = router.urls
