from django.urls import path

from salespurchasing.views.users import UserLogin

app_name = 'api'

urlpatterns = [
    path('UserLogin/', UserLogin.as_view(), name='UserLogin'),
]