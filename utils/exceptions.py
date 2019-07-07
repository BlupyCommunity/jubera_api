from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import ugettext_lazy as _


class ValidateError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Validate Error.')
    default_code = 'validate_error'


