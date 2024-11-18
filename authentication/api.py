import json
from django.http import JsonResponse
from django.views import View
from .validations import authentication_validation
from django.contrib.auth.models import User


class LoginApi(View):

    def post(self, request):
        # obtener datos del request en formato JSON
        data = json.loads(request.body)

        # validar los datos del login
        errors = authentication_validation().validate_login(data)
        if errors:
            return JsonResponse({'errors': errors}, status=400)
        # obtener el usuario
        print(data["email"])
        user = User.objects.filter(email=data['email']).first()

        if not user or not user.check_password(data['password']):
            errors.append({'field': 'email', 'error': 'Invalid credentials' })
            return JsonResponse({'errors': errors}, status=401)

        # serializar el usuario
        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

        # respuesta
        return JsonResponse({'message': 'Login successful', 'errors': errors, 'user': user_data}, status=200)
