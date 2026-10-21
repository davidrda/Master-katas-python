# Ejercicio 10
#
# Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.


# Escribe tu solución aquí
class ErrorListaVacia(Exception):
    pass


def calcular_promedio(lista):

    if not lista:
        raise ErrorListaVacia("No puedes insertar una lista vacía")

    promedio = sum(lista) / len(lista)

    return round(promedio, 2)


# Separación de responsabilidades, se maneja el error fuera
try:
    calculo = calcular_promedio([2, 5, 7, 5, 2, 1])
    print(calculo)

except ErrorListaVacia as e:
    print(f"Error: {e}")

    

