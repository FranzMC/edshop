from django.http import JsonResponse
from .models import Estudiante, Examen, ExamenPreguntas, Pregunta
from web.utils.opencv_scanner import detectar_respuestas
from web.utils.pdf_generator import generar_pdf_examen

def generar_examen(estudiante_id, cantidad_preguntas):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    examen = Examen.objects.create(titulo="Nuevo Examen", fecha="2025-06-10", estudiante=estudiante)
    
    preguntas = list(Pregunta.objects.all())
    seleccionadas = random.sample(preguntas, cantidad_preguntas)

    for pregunta in seleccionadas:
        ExamenPreguntas.objects.create(examen=examen, pregunta=pregunta)

    return JsonResponse({"examen_id": examen.id, "mensaje": "Examen generado con éxito."})

def evaluar_examen(request, estudiante_id, examen_id):
    examen = Examen.objects.get(id=examen_id)
    respuestas_marcadas = detectar_respuestas("examen_capturado.jpg")

    correctas = sum(1 for i, pregunta in enumerate(ExamenPreguntas.objects.filter(examen=examen))
                    if respuestas_marcadas[i] == pregunta.pregunta.correcta)
    total_preguntas = ExamenPreguntas.objects.filter(examen=examen).count()
    resultado = (correctas / total_preguntas) * 100

    return JsonResponse({"estudiante": examen.estudiante.nombre, "examen": examen.titulo, "calificacion": resultado})