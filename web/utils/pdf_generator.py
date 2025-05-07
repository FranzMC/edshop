from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from web.models import Examen, ExamenPreguntas

def generar_pdf_examen(examen_id):
    examen = Examen.objects.get(id=examen_id)
    archivo_pdf = f"Examen_{examen_id}.pdf"
    
    c = canvas.Canvas(archivo_pdf, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Examen: {examen.titulo}")
    c.drawString(100, 730, f"Estudiante: {examen.estudiante.nombre}")

    y = 700
    for pregunta in ExamenPreguntas.objects.filter(examen=examen):
        c.drawString(100, y, pregunta.pregunta.texto)
        y -= 30

    c.save()
    return archivo_pdf