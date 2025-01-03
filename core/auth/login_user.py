from django.db.models import Q
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from ..models.user import User


User = get_user_model()

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def LoginUser(request):
    email = request.data.get("email")
    password = request.data.get("password")
    print("Email:", email)
    print("Password:", password)

    if email is not None and password is not None:
        try:
            user = User.objects.get(Q(email=email))
            print("Stored Password:", user.password)
            print("Password Check:", check_password(password, user.password))
            print("Is user active:", user.is_active)

            user_auth = authenticate(email=email, password=password)
            print("Authentication result:", user_auth)

            if user_auth is not None:
                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user_auth)

                response_data = {
                    "refresh": str(refresh),
                    "access": str(access),
                    "email": user_auth.email,
                    "id": user_auth.id,
                    "group": [group.name for group in user_auth.groups.all()],
                    "message": "Login realizado com sucesso!"
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                print("Authentication failed for the user")

        except User.DoesNotExist:
            user = None
            print("User not found in the database")
            
    else:
        return Response(
            {"message": "Credenciais inválidas!"}, status=status.HTTP_400_BAD_REQUEST
        )

    print("Final user object:", user)

    return Response(
        {"message": "Credenciais inválidas!"},
        status=status.HTTP_400_BAD_REQUEST
    )