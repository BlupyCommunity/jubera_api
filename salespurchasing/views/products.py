from rest_framework import authentication, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from salespurchasing.models import Product
from salespurchasing.serializers import ProductSerializer
from utils.exceptions import ValidateError
from utils.models import auto_number


class ProductNew(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def check_pass(self, request):
        data = request.data

        if data.get('name') is None:
            raise ValidateError("Nama produk tidak boleh kosong")

        if data.get('unit') is None:
            raise ValidateError('Satuan produk tidak boleh kosong')

        if data.get('sales_price') is None:
            raise ValidateError('Harga jual tidak boleh kosong')

        if data.get('stock') is None:
            raise ValidateError('Stok tidak boleh kosong')

        if isinstance(data.get('sales_price'), int) is False:
            raise ValidateError('Harga jual harus angka')

        if isinstance(data.get('stock'), int) is False:
            raise ValidateError('Stok harus angka')

    def execute(self, request):
        data = request.data
        products = Product.objects.all()
        product = Product.objects.create(
            sku=auto_number(products, prefix='PRD'),
            name=data.get('name'),
            unit=data.get('unit').upper(),
            sales_price=data.get('sales_price'),
            stock=data.get('stock')
        )

        return product

    def post(self, request):
        self.check_pass(request)
        product = self.execute(request)

        return Response(ProductSerializer(product, many=False).data)


class ProductList(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.GET.get('name')
        sku = self.request.GET.get('sku')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if sku:
            queryset = queryset.filter(sku=sku)

        return queryset


class ProductDetail(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def check_pass(self, request):
        data = request.data

        if data.get('id') is None:
            raise ValidateError('ID tidak boleh kosong')

        products = Product.objects.filter(pk=data.get('id'))
        if not products:
            raise ValidateError('Produk tidak ada')

    def execute(self, request):
        data = request.data
        product = Product.objects.get(pk=data.get('id'))

        return product

    def post(self, request):
        self.check_pass(request)
        product = self.execute(request)

        return Response(ProductSerializer(product, many=False).data)


class ProductUpdate(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def check_pass(self, request):
        data = request.data

        if data.get('id') is None:
            raise ValidateError('ID tidak boleh kosong')

        products = Product.objects.filter(pk=data.get('id'))
        if not products:
            raise ValidateError('Produk tidak ada')

        if data.get('name') is None:
            raise ValidateError("Nama produk tidak boleh kosong")

        if data.get('unit') is None:
            raise ValidateError('Satuan produk tidak boleh kosong')

        if data.get('sales_price') is None:
            raise ValidateError('Harga jual tidak boleh kosong')

        if data.get('stock') is None:
            raise ValidateError('Stok tidak boleh kosong')

        if isinstance(data.get('sales_price'), int) is False and isinstance(data.get('sales_price'), float) is False:
            raise ValidateError('Harga jual harus angka')

        if isinstance(data.get('stock'), int) is False:
            raise ValidateError('Stok harus angka')

    def execute(self, request):
        data = request.data
        product = Product.objects.get(pk=data.get('id'))
        is_change = False

        if product.name != data.get('name'):
            product.name = data.get('name')
            is_change = True

        if product.unit != data.get('unit').upper():
            product.unit = data.get('unit').upper()
            is_change = True

        if product.sales_price != data.get('sales_price'):
            product.sales_price = data.get('sales_price')
            is_change = True

        if product.stock != data.get('stock'):
            product.stock = data.get('stock')
            is_change = True

        if is_change:
            product.save()

        return product

    def post(self, request):
        self.check_pass(request)
        product = self.execute(request)

        return Response(ProductSerializer(product, many=False).data)

