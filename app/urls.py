from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from core.router import urlpatterns as router_urls
from core.auth.login_user import LoginUser
from core.auth.forgot_password import ForgotPasswordUser
from core.auth.reset_password import ResetPasswordUser

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # API
    path('api/', include(router_urls)),  
    path("api/login/", LoginUser, name="login"),
    path("api/forgot-password/", ForgotPasswordUser, name="forgot-password"),
    path("api/reset-password/", ResetPasswordUser, name="reset-password"),
]