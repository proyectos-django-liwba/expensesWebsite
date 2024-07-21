# Proyecto django tutorial

## Comandos base de Proyecto

1. Crear entorno virtual
```  
  python -m venv ./venv
```
   
2.  Activar el entorno virtual
```
    python -m venv ./venv/bin/activate
```

3. Crear un proyecto 
```   
    django-admin startproject <my_project>
```  
   
4. Crear una aplicación 
```   
    django-admin startapp <my_app>
```  
   
5. Compilar el proyecto 
```   
    python manage.py runserver
``` 
   
6. Generar archivo requirements.txt, si no lo tenemos o queremos actualizarlo
```   
  pip freeze > requirements.txt
```  
   
7. Install requirements 
```   
  pip install -r requirements.txt
```

8. Crear migraciones 
```   
  python manage.py migrate
```

9. Crear super usuario
```   
    python manage.py createsuperuser
```
   
10. Crear archivos estaticos
```
   python manage.py collectstatic
```  
   
### Instalar Dependencias 

##### Django
```   
    pip install django
```  
##### Instalar django rest framework ✅
```   
    pip install djangorestframework
```

   - Documentacion [djangorestframework](https://www.django-rest-framework.org/)
   - Requiere configurar el archivo settings.py, para agregar rest_framework
  
```  
     INSTALLED_APPS = [
         ...
         'rest_framework',
     ]
```  
##### Instalar drf-yasg ✅

```
    pip install -U drf-yasg
```
- Requiere configurar el archivo settings.py, para agrear drf_yasg
- Requiere configurar el archivo settings.py, para definir rutas estaticas
- Requiere configurar el archivo urls.py, para agrear drf_yasg
- Documentacion [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html#usage)
```
    pip install setuptools
```
- Agregar los archivos estaticos y configurar la dependencia en settings.py 
```
   INSTALLED_APPS = [
     ...
     'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
     'drf_yasg',
   ]
   STATIC_URL = '/static/'
   STATIC_ROOT = './static/'
```
- Generar achivos estaticos
```
   python manage.py collectstatic
```
  
- Configurar la dependencia en urls.py

```
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi
    
    name_api = 'Django Project'
    schema_view = get_schema_view(
       openapi.Info(
          title=f"Documentación de la API {name_api}",
          default_version='v1',
          description=f"Documentación de la API {name_api}",
          terms_of_service="https://www.google.com/policies/terms/",
          contact=openapi.Contact(email="djangoproject@correo.com"),
          license=openapi.License(name="BSD License"),
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
    )
    
    urlpatterns =  [
        path('admin/', admin.site.urls),
        path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
```
##### Configurar PostgreSQL ✅
```
    pip install psycopg2
```
- Paquetes necesarios para que funcione el conector
```
    sudo apt install libpq-dev python3-dev build-essential
```
- Crear la base de datos, necesitamos crear una base de datos en posgreSQL

- Configurar la conexion con la base de datos, settings.py

```
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME':  'db_expenses',
          'USER': 'postgres',
          'PASSWORD': 'Admin1234',
          'HOST': '127.0.0.1',
          'PORT': '5432'
      }
    }
```
  
# Interfaces en Django

### Crear template base
Con el fin de reutilizar codigo html podemos crear template base, para agilizar la creación de vistas.
Creamos nuestro archivo dentro de la carpeta template, base.html con nuestro codigo html base.

```
    <html lang="en">
    <head>
    
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    
        <title>My title </title>
    
    </head>
    <body>
    
    </body>
    </html>
```

### Configurar e implementar archivos estáticos
En Django usualmente tiene configurado el acceso a archivos de template, 
pero los estaticos debemos configurarlos en settings.py

1. Importamos os
```
    import os
```
Recordar la existencia de esta variable creada por defecto al crear un proyecto en django, nos ayuda
a crear rutas relativas de forma dinamica.
```
    BASE_DIR = Path(__file__).resolve().parent.parent
```
2. Agregamos la ubicación de los estaticos
```
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
```
De esta forma los estáticos serán accesibles en los templates

Recordar que con un comando se crear la carpeta y archivos estáticos asociados a dependencias instaladas
```
   python manage.py collectstatic
```  
3. Uso de archivos estáticos en templates
```
    {% load static %}
```
Recordar que en la carpeta static usualmente crearemos directorios para archivos como imagenes,
js, css etc..

```
    {% load static %}
    <html lang="en" >
    <head>
    
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Expenses WebSite</title>
    
        <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
        <link rel="stylesheet" href="{% static '/css/estilos.css' %}">
        <link rel="stylesheet" href="{% static 'css/dashboard.css' %}">
    
    </head>
    <body>
    
    
    <script src="{% static 'js/jquery-3.7.1.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    <script src="{% static 'js/scripts.js' %}"></script>
    <script src="{% static 'js/theme-color.js' %}"></script>
    </body>
    </html>
```
De esta forma nuestro templates reconocerán los archivos estáticos que deseamos implementar

### Insertar segmentos de condigo html dentro de un template
En ocaciones es mas practico y legible segmentar el codigo por componentes, para ello se pueden
crear una carpeta dentro de templates llamada por ejemplo partials o components, y crearmos dentro de ella
nuestro segmentos de codigo.

1. Creamos un archivo ejemplo: _card.html
```
<div class="card">
  <div class="card-body">
    This is some text within a card body.
  </div>
</div>
```
En este caso utilizamos boostrap, en un punto anterior implementamos los estaticos

2. Agregar el componente en una vista
```
{% load static %}
<html lang="en" data-bs-theme="auto">
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Expenses WebSite</title>

    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static '/css/estilos.css' %}">
    <link rel="stylesheet" href="{% static 'css/dashboard.css' %}">

</head>
<body class="vh-100">

{% include 'partials/_card.html' %}

<script src="{% static 'js/jquery-3.7.1.min.js' %}"></script>
<script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
<script src="{% static 'js/scripts.js' %}"></script>
<script src="{% static 'js/theme-color.js' %}"></script>
</body>
</html>
```
3. Agregar estaticos propios de una vista
```
{% extends 'base-auth.html' %}

{% load static %}

{% block content %}

    <div class="card">
      <div class="card-body">
        This is some text within a card body.
      </div>
    </div>
    
   <script src="{% static 'js/card.js' %}"></script>

{% endblock %}
```

### Uso de props en vistas
Son variables que creamos con el fin de modificar el contenido de forma dinamica o realizar 
procesos logicos y luego mostrar el resultado

1. Implemetación dentro de la vista
```
{% load static %}
<html lang="en" data-bs-theme="auto">
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Expenses WebSite -{{ title }}</title>

    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static '/css/estilos.css' %}">
    <link rel="stylesheet" href="{% static 'css/dashboard.css' %}">

</head>
<body class="vh-100">

{% include 'partials/_icons_base.html' %}

{% include 'partials/_theme_color.html' %}

{% include 'partials/_navbar.html' %}


<script src="{% static 'js/jquery-3.7.1.min.js' %}"></script>
<script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
<script src="{% static 'js/scripts.js' %}"></script>
<script src="{% static 'js/theme-color.js' %}"></script>
</body>
</html>

```
De esta forma `{{ nombre_variable }}` accedemos a la variable para mostrar su contenido

2. Crear la variable o props a mostrar
```
from django.shortcuts import render

def index(request):
    return render(request, 'expenses/index.html', {'title': 'Home'})

```
Dentro del archivo views.py de nuestra app, el cual retorna la vista que deseamos mostrar
lograr declarar la variable o props que cambiar de forma dinamica en nuestro template base,
con el nombre de la pagina. En este segmento de codigo: `{'nombre_variable': valor}`

### uso de variables de contexto
Cuando necesitemos crear variables de acceso a multiples vistas podemos hacer uso de variables
de contexto las cuales no deben declarar de forma individual en cada vista.

- Configuración
```
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates']
            ,
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...
                    'context.custom_context.current_year', # Agregamos esta linea
                ],
            },
        },
    ]
```
Modificamos el archivo settings.py, agregando una linea la cual contiene el nombre de la carpeta
o app donde creamos un archivo y una funcion que retorna el valor de nuestra variable o diccionario al contexto
Directirio: /context/custom_context.py 
La funcion que retorna la variable en este caso se llama current_year

2. Crear archivo de contexto
```
from datetime import datetime

def current_year(request):
    return {
        'current_year': datetime.now().year,
    }

```

3. Uso de la variable de contexto en un template
```
    <footer>
        <p class="mt-5 mb-3 text-body-secondary text-center ">&copy; 2020–{{ current_year }}
        </p>
    </footer>
```

De esta forma en todas las vistas tengo acceso a la variable `current_year`

### Inyectar contenido de forma dinamica
En con el fin de reduccir codigo y sacarle el maximo provecho a archivos de template base
inyectaremos codigo a nuestras vistas. 

1. Página o Vista
```
    {% extends 'base.html' %}
    
    {% block content %}
        <h3 class="my-3">Add expenses</h3>
    {% endblock %}
```
2. Template base
```
    {% load static %}
    <html lang="en" data-bs-theme="auto">
    <head>
    
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
         <!-- SEO -->
        <meta name="description" content="Proyecto de practica Django">
        <meta name="author" content="liwBh">
        <meta name="keywords" content="Django, Expenses, Web Development, Project, Python">
    
        <title>Expenses WebSite -{{ title }}</title>
    
        <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
        <link rel="stylesheet" href="{% static '/css/estilos.css' %}">
        <link rel="stylesheet" href="{% static 'css/dashboard.css' %}">
    
        <!-- Favicon -->
        <link rel="icon" href="{% static 'img/favicon.ico' %}">
        <meta name="theme-color" content="#000000">
    
        <!-- icons -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.min.css" rel="stylesheet">
    
    </head>
    <body class="vh-100">
    
    {% include 'partials/_icons_base.html' %}
    
    {% include 'partials/_theme_color.html' %}
    
    {% include 'partials/_navbar.html' %}
    
    <div class="container-fluid">
        <div class="row">
    
            {% include 'partials/_sidebar.html' %}
    
            <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                {% block content %}
                {% endblock %}
    
            </main>
        </div>
    </div>
    
    <script src="{% static 'js/jquery-3.7.1.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    <script src="{% static 'js/scripts.js' %}"></script>
    <script src="{% static 'js/theme-color.js' %}"></script>
    </body>
    </html>

```

Con `extends` reutilizamos nuestra vista base ademas, le inyectamos de forma dinamica con `block`
el contenido propio de nuestra vista.

### Uso de url en enlaces
```
<a href="{% url 'register' %}" >Registrarse</a>
```

De forma mas practica en lugar colar un url completa `http://localhost:8000/authentication/register/`
que luego en producción debemos cambiar es mas practico utilizar `url` y 'nombre_vista'.

El nombre de la vista debe ser unico y se lo asignamos cuando creamos una url en el archivo urls.py
```
from django.urls import path
from .views import RegisterView, LoginView, ResetPasswordView, ForgotPasswordView

urlpatterns = [
   path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
]

```
### Compartir datos o props con un componente

1. Obtener una lista de objetos en el archivo views.py de la app
```
from django.shortcuts import render
from .models import Expense

def expenses_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/index.html', {'expenses': expenses})

```
Obtenemos la lista de gastos almacenada en base de datos, luego la compartimos con la vista

2. En nuestra vista principal iteramos la lista de objetos

```
    {% extends 'base.html' %}
    
    {% block content %}
        <h1>Expenses List</h1>
        <div class="expenses-container">
            {% for expense in expenses %}
                 {% include 'expenses/components/card.html' with expense=expense %}
            {% endfor %}
        </div>
    {% endblock %}
```
En el segmento de codigo iteramos la lista, y vamos a compartir el diccionario o datos
con un componente. Se puede compartir mas de una variable `with nombre_prop1=variable1 nombre_prop2=variable2 ...`

3. Consumir datos de las props en el componente
```
    <!-- card component -->
    <div class="card">
        <h2>{{ expense.name }}</h2>
        <p>Price: ${{ expense.price }}</p>
    </div>
```
## Formularios 

### Permisos en formulario
- Similar a otros framework para usar un formulario requiere permisos csrf
```
    <form id="form-login" autocomplete="off">
        {% csrf_token %}
    </form>
```
- También en al utilizar herramientas como postman o insomnia, se deben agregar a la url
```
    from django.urls import path
    from .views import LoginView
    from .api import LoginApi
    from django.views.decorators.csrf import csrf_exempt
    
    urlpatterns = [
        path('login/', LoginView.as_view(), name='login'),
        path('api/login/', csrf_exempt(LoginApi.as_view()), name='api-login'),
    ]
```

### Enviar datos por formulario
En el directorio de una app creamos un archivo api.py, en donde se recibirá los datos,
se realizaran acciones como: consultas a bd, procedimientos logicos, respuestas a solicitudes

1. Endpoint de API
```
import json
from django.http import JsonResponse
from rest_framework.views import View
from .validation import authentication_validation


class LoginApi(View):

    def post(self, request):
        # obtener datos del request y decodificar el json
        data = json.loads(request.body)
        # validaciones
        errors = authentication_validation().validate_login(data)

        if errors:
            return JsonResponse({'errors': errors}, status=400)
            
        # consultas a bd
        # procedimientos logicos
        # respuesta
        return JsonResponse({'message': 'Login successful', 'errors': errors}, status=200)

```

2. Creamos un archivo para las validaciones dentro del directorio de la app, validations.py
```
class authentication_validation():
    # data contiene todos los datos del formulario
    # se accede a ellos por el name que se les dio en el form
    
    def validate_login(self, data):
        print(data)
        errors = []
        # validamos que existan las variables y que no esten vacias
        if data["email"] is None or not data["email"]:
            errors.append({'field': 'email', 'error': 'Email is required' })
        if data["password"] is None or not data["password"]:
            errors.append({'field': 'password', 'error': 'Password is required' })

        return errors
```
3. Crear form
```
    <form id="form-login" autocomplete="off">
        {% csrf_token %}

        <div class="form-floating" id="email_container">
            <input type="email" id="email" name="email" class="form-control radius-top" placeholder="name@example.com">
            <label for="email">Email address</label>
            <p class="feedback"></p>
        </div>
        <div class="form-floating" id="password_container">
            <input type="password" id="password" name="password" class="form-control radius-bottom password-input "
                   placeholder="Password">
            <label for="password">Password</label>
            <i class="bi bi-eye-fill show-password"></i>
            <p class="feedback"></p>
        </div>

        <button class="btn btn-primary w-100 py-2" type="submit">Login</button>

    </form>
```
4. Comunicar el form de la vista con el endpoint 
```
document.addEventListener('DOMContentLoaded', function () {
    const formLogin = document.getElementById('form-login');

    formLogin.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(this);

        // Convierte FormData a un objeto
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Enviar la petición al endpoint de la API
        fetch('http://localhost:8000/authentication/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(result => {
                // verificar la respuesta y errores
                console.log('Response:', result);
                console.log(result.errors.length)
                

                if (result.errors.length > 0) {
                    // Mostrar los errores en el formulario
                    handleValidationErrors(result.errors);
                ...
                }
                
                // mostrar notificación de respuesta
                ...
            })
            .catch(error => {
                console.error('Error:', error);
            });

    });
});

//validación de formulario de login
function handleValidationErrors(errors) {
    errors.forEach(error => {
        const fieldContainer = document.getElementById(`${error.field}_container`);
        const input = fieldContainer.querySelector('input');
        const feedback = fieldContainer.querySelector('.feedback');

        input.classList.add('border-1', 'border-danger');
        feedback.innerHTML = error.error;
    });

    setTimeout(() => {
        errors.forEach(error => {
            const fieldContainer = document.getElementById(`${error.field}_container`);
            const input = fieldContainer.querySelector('input');
            const feedback = fieldContainer.querySelector('.feedback');

            input.classList.remove('border-1', 'border-danger');
            feedback.innerHTML = '';
        });
    }, 2000);
}
```

### Libreria de Notificaciones

["Documentación Toastify"](https://www.npmjs.com/package/toastify-js)

1. CDN de la libreria
```
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/toastify-js/src/toastify.min.css">
    
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/toastify-js"></script>
```

2. Uso solo mostrar mensaje
```
    Toastify({
        text: "This is a success message!",
        duration: 3000,
        gravity: "top", // or bottom
        position: "right", // or left
        backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
        stopOnFocus: true, // Prevents dismissing of toast on hover
    }).showToast();
```
3. Uso con funcion callback
```
    Toastify({
      text: "This is a toast",
      duration: 3000,
      destination: "https://github.com/apvarun/toastify-js",
      newWindow: true,
      close: true,
      gravity: "top", // `top` or `bottom`
      position: "left", // `left`, `center` or `right`
      stopOnFocus: true, // Prevents dismissing of toast on hover
      style: {
        background-color: "linear-gradient(to right, #00b09b, #96c93d)",
      },
      onClick: function(){} // Callback after click
    }).showToast();
```