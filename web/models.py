from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=50, unique=True)

class Examen(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

class Pregunta(models.Model):
    texto = models.CharField(max_length=300)
    correcta = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

class ExamenPreguntas(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

class Respuesta(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    seleccionada = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def es_correcta(self):
        return self.seleccionada == self.pregunta.correcta