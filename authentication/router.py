import json

from django.http import JsonResponse
from rest_framework.views import View

from .validation import authentication_validation


class LoginApi(View):

    def post(self, request):
        data = json.loads(request.body)

        errors = authentication_validation().validate_login(data)

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        return JsonResponse({'message': 'Login successful'}, status=200)
