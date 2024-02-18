from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginSerializer
from rest_framework import permissions, status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenObtainPairSerializerWithUsername(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class TokenObtainPairWithUsernameView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializerWithUsername


class UserLogin(APIView):
    # permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)

    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.check_user(data)
            login(request, user)
            request.session['authenticated_user'] = user.username
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)

    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "You are not logged in!"}, status=status.HTTP_400_BAD_REQUEST)
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserSession(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)

    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        print(request.headers)
        data = {"is_authenticated": False, "username": ""}
        if request.user.is_authenticated:
            data.update({"is_authenticated": True, "username": request.user.username})
        print("Before validate response", data, request.user, request.user.is_authenticated, request.session.keys(), request.session.values(), request.session.session_key)
        return Response(data, status=status.HTTP_200_OK)
