from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import login, authenticate
from .serializers import RegistrationSerailizer, LoginSerializer


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerailizer


class LoginView(APIView):
    def post(self, request, format=None):
        login_serializer = LoginSerializer(data=request.data)

        if login_serializer.is_valid(raise_exception=True):
            user = authenticate(**login_serializer.validated_data)

            if user is not None:
                login(request, user)

                return Response({'detail': 'Успешно вошли в систему'}, status=status.HTTP_200_OK)
            return Response({'detail': 'Пользователь с такими данными не найден'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_username(request):
    username = request.user.username
    return Response({'username': username}, status=status.HTTP_200_OK)
