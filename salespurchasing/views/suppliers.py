from rest_framework import authentication, permissions
from rest_framework.views import APIView


class SupplierNew(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def check_pass(self, request):
        pass

    def execute(self, request):
        pass

    def post(self, request):
        pass