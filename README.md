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