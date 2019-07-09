from django.db import transaction
from rest_framework import authentication, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from salespurchasing.models import Supplier
from salespurchasing.serializers import SupplierSerializer
from utils.exceptions import ValidateError
from utils.models import auto_number


class SupplierNew(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def check_pass(self, request):
        data = request.data

        if data.get('name') is None:
            raise ValidateError('Nama tidak boleh kosong')

        if data.get('address') is None:
            raise ValidateError('Alamat tidak boleh kosong')

        if data.get('phone') is None:
            raise ValidateError('Nomer telepon tidak boleh kosong')

    @transaction.atomic()
    def execute(self, request):
        data = request.data

        supplier = Supplier.objects.create(
            supplier_code=auto_number(Supplier.objects.all()),
            name=data.get('name'),
            address=data.get('address'),
            phone=data.get('phone')
        )

        return supplier

    def post(self, request):
        self.check_pass(request)
        supplier = self.execute(request)

        return Response(SupplierSerializer(supplier, many=False).data)


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



