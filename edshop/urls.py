from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),  # Asegúrate de incluir las rutas de la app 'web'
]
