from django.core.mail import send_mail

def enviar_resultado(estudiante, resultado):
    mensaje = f"Hola {estudiante.nombre}, tu calificación en el examen fue: {resultado}%."
    send_mail(
        "Resultados del Examen",
        mensaje,
        "admin@evaluador.com",
        [estudiante.email],
        fail_silently=False,
    )