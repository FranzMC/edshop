from django.contrib import admin
from .models import Estudiante, Examen, Pregunta, Respuesta  # Asegúrate de que Respuesta esté aquí

admin.site.register(Estudiante)
admin.site.register(Examen)
admin.site.register(Pregunta)
admin.site.register(Respuesta)  # También registra el modelo aquí