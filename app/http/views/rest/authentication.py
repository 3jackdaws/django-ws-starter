from rest_framework.views import APIView, Request, Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'groups')


# /api/auth-sessions
class AuthenticationView(APIView):

    def get(self, request: Request):
        user = request.user  # type: User
        if user.is_anonymous:
            return Response(status=403)
        else:
            return Response(UserSerializer(instance=user).data)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {}
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response(UserSerializer(instance=user).data)
            else:
                return Response(status=401)
