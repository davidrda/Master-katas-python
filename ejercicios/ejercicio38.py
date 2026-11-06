# Ejercicio 38
#
# Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
#
# - Reglas:
#     0 - 69: insuficiente
#     70 - 79: bien
#     80 - 89: muy bien
#     90 - 100: excelente


# Escribe tu solución aquí

def determinar_calificacion(entrada):

    calificacion = int(entrada)

    if calificacion < 0 or calificacion > 100:
        raise ValueError("Introduce una calificación válida")

    if calificacion >= 90:
        return "excelente"

    if calificacion >= 80:
        return "muy bien"

    if calificacion >= 70:
        return "bien"

    return "insuficiente"

alumnos = [
    {
        "nombre": "David",
        "calificacion": 100
    },
    {
        "nombre": "Adrian",
        "calificacion": 69
    }
]

for alumno in alumnos:
    try:
        print(f"La calificación de {alumno["nombre"]} es {determinar_calificacion(alumno["calificacion"])}")
    except ValueError as e:
        print(f"Error: {e}")

