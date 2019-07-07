from django.urls import path

from salespurchasing.views.users import UserLogin, UserNew, UserUpdate, UserList, UserDetail

app_name = 'api'

urlpatterns = [
    path('UserLogin/', UserLogin.as_view(), name='UserLogin'),
    path('UserNew/', UserNew.as_view(), name='UserNew'),
    path('UserDetail/', UserDetail.as_view(), name='UserDetail'),
    path('UserUpdate/', UserUpdate.as_view(), name='UserUpdate'),
    path('UserList/', UserList.as_view(), name='UserList'),
]