from rest_framework import authentication, permissions, generics
from rest_framework.views import APIView

from salespurchasing.models import Supplier
from salespurchasing.serializers import SupplierSerializer


class SupplierNew(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def check_pass(self, request):
        pass

    def execute(self, request):
        pass

    def post(self, request):
        pass


class SupplierList(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

    def get_queryset(self):
        queryset = Supplier.objects.all()
        supplier_code = self.request.GET.get('supplierCode')
        name = self.request.GET.get('name')

        if supplier_code:
            queryset = queryset.filter(supplier_code=supplier_code)

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class SupplierDetail(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def check_pass(self, request):
        pass

    def execute(self, request):
        pass

    def post(self, request):
        pass


class SupplierUpdate(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def check_pass(self, request):
        pass

    def execute(self, request):
        pass

    def post(self, request):
        pass



