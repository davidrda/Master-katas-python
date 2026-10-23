# Ejercicio 18
#
# Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.


# Escribe tu solución aquí
estudiantes = []

# Validar n
while True:
    try:
        n = int(input("¿Cuántos estudiantes hay?: "))
        if n > 0:
            break
        print("Debe ser mayor que 0")
    except ValueError:
        print("Introduce un número entero")

for i in range(1, n + 1):
    nombre = input(f"Inserta el nombre del estudiante nº{i}: ")

    edad = int(input(f"Inserta la edad del estudiante nº{i}: "))
    calificacion = float(input(f"Inserta la calificación del estudiante nº{i}: "))

    estudiantes.append({"nombre": nombre, "edad": edad, "calificacion": calificacion})


estudiantes_mayor_90 = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

print("Aquí tienes el resultado: ")
print(estudiantes_mayor_90)