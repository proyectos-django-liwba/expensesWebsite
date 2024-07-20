from django.http import JsonResponse


class authentication_validation():

    def validate_login(self, data):
        print(data)
        errors = []
        if data["email"] is None or not data["email"]:
            errors.append({'field': 'email', 'error': 'Email is required' })
        if data["password"] is None or not data["password"]:
            errors.append({'field': 'password', 'error': 'Password is required' })

        return errors