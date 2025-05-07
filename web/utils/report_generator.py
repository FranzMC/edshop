import pandas as pd
import matplotlib.pyplot as plt
from .models import Estudiante, Examen

def generar_reporte():
    estudiantes = Estudiante.objects.all()
    datos = [{"Nombre": e.nombre, "Calificación": evaluar_examen("examen.jpg", e.id)} for e in estudiantes]
    
    df = pd.DataFrame(datos)
    df.to_csv("Reporte_Estudiante.csv", index=False)

    df.plot(x="Nombre", y="Calificación", kind="bar")
    plt.savefig("Reporte_Gráfico.png")