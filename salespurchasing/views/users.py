from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import generics, permissions, authentication
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
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def check_pass(self, request):
        data = request.data

        if not data.get('username'):
            raise ParseError('Username tidak boleh kosong')

        if not data.get('password'):
            raise ParseError('Password tidak boleh kosong')

        if not data.get('first_name'):
            raise ParseError('Nama depan tidak boleh kosong')

        if not data.get('last_name'):
            raise ParseError('Nama belakang tidak boleh kosong')

        if not data.get('email'):
            raise ParseError('Email tidak boleh kosong')

        users = User.objects.filter(username=data.get('username'))
        if users:
            raise ParseError('Username sudah ada')

        users = User.objects.filter(email=data.get('email'))
        if users:
            raise ParseError('Email sudah ada')

    @transaction.atomic()
    def execute(self, request):
        data = request.data

        if data.get('is_superuser', False):
            user = User.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                is_active=True,
                is_superuser=True,
                is_staff=True
            )
        else:
            user = User.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                is_active=True,
                is_superuser=False,
                is_staff=True
            )

        Token.objects.create(user=user)

        return user

    def post(self, request):
        self.check_pass(request)
        user = self.execute(request)

        return Response(UserSerializer(user, many=False).data)


class UserUpdate(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def check_pass(self, request):
        data = request.data

        if not data.get('username'):
            raise ParseError('Username tidak boleh kosong')

        if not data.get('password'):
            raise ParseError('Password tidak boleh kosong')

        if not data.get('first_name'):
            raise ParseError('Nama depan tidak boleh kosong')

        if not data.get('last_name'):
            raise ParseError('Nama belakang tidak boleh kosong')

        if data.get('is_active') is None:
            raise ParseError('Aktivasi tidak valid')

        if not isinstance(data.get('is_active'), bool):
            raise ParseError('Aktivasi tidak valid')

        if not data.get('email'):
            raise ParseError('Email tidak boleh kosong')

        if data.get('is_superuser') is None:
            raise ParseError('Hak akses tidak valid')

        if not isinstance(data.get('is_superuser'), bool):
            raise ParseError('Hak akses tidak valid')

        users = User.objects.filter(username=data.get('username'))
        if not users:
            raise ParseError('Username tidak terdaftar')

        user = User.objects.get(username=data.get('username'))
        emails = User.objects.filter(email=data.get('email')).exclude(username=user.username)

        if emails:
            raise ParseError('Email telah terdaftar')

        if not data.get('username_new'):
            raise ParseError('Username yang baru tidak valid')

        usernames = User.objects.filter(username=data.get('username_new')).exclude(username=user.username)
        if usernames:
            raise ParseError('Username telah terdaftar sebelumnya')


    @transaction.atomic()
    def execute(self, request):
        data = request.data

        user = User.objects.get(username=data.get('username'))

        if user.first_name != data.get('first_name'):
            user.first_name = data.get('first_name')

        if user.last_name != data.get('last_name'):
            user.last_name = data.get('last_name')

        if user.email != data.get('email'):
            user.email = data.get('email')

        if user.is_superuser != data.get('is_superuser'):
            user.is_superuser = data.get('is_superuser')

        if not user.check_password(data.get('password')):
            user.set_password(data.get('password'))

        if user.is_superuser != data.get('is_superuser'):
            user.is_superuser = data.get('is_superuser')

        if user.is_active != data.get('is_active'):
            user.is_active = data.get('is_active')

        if user.username != data.get('username_new'):
            user.username = data.get('username_new')

        user.save()

        Token.objects.get(user=user).delete()
        Token.objects.create(user=user)

        return user

    def post(self, request):
        self.check_pass(request)
        user = self.execute(request)

        return Response(UserSerializer(user, many=False).data)


class UserList(generics.ListAPIView):
    pass

