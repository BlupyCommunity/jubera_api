from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from salespurchasing.serializers import UserSerializer


class UserLogin(APIView):
    def check_pass(self, request):
        data = request.data

        if not data.get('username'):
            raise ParseError('Username tidak boleh kosong')

        if not data.get('password'):
            raise ParseError('Password tidak boleh kosong')

        users = User.objects.filter(username=data.get('username'))
        if not users:
            raise ParseError('Username tidak terdaftar')

        user = User.objects.get(username=data.get('username'))
        if not user.check_password(data.get('password')):
            raise ParseError('Password tidak cocok')

    def execute(self, request):
        data = request.data

        user = User.objects.get(username=data.get('username'))
        token, created = Token.objects.get_or_create(user=user)

        return user

    def post(self, request):
        self.check_pass(request)
        user = self.execute(request)

        return Response(UserSerializer(user, many=False).data)


class UserNew(APIView):
    pass


class UserUpdate(APIView):
    pass


class UserDisabled(APIView):
    pass


class UserList(generics.ListAPIView):
    pass

