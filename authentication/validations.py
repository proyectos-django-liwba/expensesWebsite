from validate_email import validate_email

class authentication_validation():

    def validate_login(self, data):
        print(data)
        errors = []
        if data["email"] is None or not data["email"]:
            errors.append({'field': 'email', 'error': 'Email is required' })
        if data["password"] is None or not data["password"]:
            errors.append({'field': 'password', 'error': 'Password is required' })

        if not validate_email(data["email"]):
            errors.append({'field': 'email', 'error': 'Invalid email format' })

        if not str(data["password"]).isalnum():
            errors.append({'field': 'password', 'error': 'Password must contain only alphanumeric characters' })

        return errors