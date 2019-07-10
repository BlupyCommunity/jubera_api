from django.urls import path

from salespurchasing.views.products import ProductNew, ProductList
from salespurchasing.views.suppliers import SupplierNew, SupplierList, SupplierDetail, SupplierUpdate
from salespurchasing.views.users import UserLogin, UserNew, UserUpdate, UserList, UserDetail

app_name = 'api'

urlpatterns = [
    path('UserLogin/', UserLogin.as_view(), name='UserLogin'),
    path('UserNew/', UserNew.as_view(), name='UserNew'),
    path('UserDetail/', UserDetail.as_view(), name='UserDetail'),
    path('UserUpdate/', UserUpdate.as_view(), name='UserUpdate'),
    path('UserList/', UserList.as_view(), name='UserList'),

    path('SupplierNew/', SupplierNew.as_view(), name='SupplierNew'),
    path('SupplierList/', SupplierList.as_view(), name='SupplierList'),
    path('SupplierDetail/', SupplierDetail.as_view(), name='SupplierDetail'),
    path('SupplierUpdate/', SupplierUpdate.as_view(), name='SupplierUpdate'),

    path('ProductNew/', ProductNew.as_view(), name='ProductNew'),
    path('ProductList/', ProductList.as_view(), name='ProductList'),
]