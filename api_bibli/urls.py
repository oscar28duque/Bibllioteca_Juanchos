"""
URL configuration for api_bibli project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#importa el modulo de administracion de Django 
from django.contrib import admin
#importa las funciones path e include del modulo de URLs  de Django 
from django.urls import path, include

#Define la lista de patrones de URL para el proyecto 
urlpatterns = [
    #ruta para la interfaz de administracion de Django 
    path('admin/', admin.site.urls),
    #incluye  las URLs definidas  en el archivo urls.py de la aplicacion 'api.app'
    #path('api/',include('api_app.urls'))
]
