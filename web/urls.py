from django.urls import path
from .views import generar_examen

urlpatterns = [
    path('generar_examen/<int:estudiante_id>/<int:cantidad_preguntas>/', generar_examen, name='generar_examen'),
]