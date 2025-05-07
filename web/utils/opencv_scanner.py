import cv2
import numpy as np

def detectar_respuestas(imagen_path):
    imagen = cv2.imread(imagen_path, cv2.IMREAD_GRAYSCALE)
    _, imagen_bin = cv2.threshold(imagen, 150, 255, cv2.THRESH_BINARY_INV)

    circulos = cv2.HoughCircles(imagen_bin, cv2.HOUGH_GRADIENT, 1, 20,
                                param1=50, param2=30, minRadius=5, maxRadius=20)

    respuestas = []
    if circulos is not None:
        circulos = np.uint16(np.around(circulos))
        for i in circulos[0, :]:
            respuestas.append((i[0], i[1]))  # Coordenadas del círculo detectado

    return respuestas