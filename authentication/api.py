import json
from django.http import JsonResponse
from django.views import View
from .validations import authentication_validation
from django.contrib.auth.models import User


class LoginApi(View):

    def post(self, request):
        data = json.loads(request.body)
        errors = authentication_validation().validate_login(data)

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        return JsonResponse({'message': 'Login successful', 'errors': errors}, status=200)
