# Ejercicio 25
#
# Crea una función que cuente el número de caracteres en una cadena de texto dada.


# Escribe tu solución aquí

def caracteres_totales(texto):

    if not isinstance(texto, str):
        raise TypeError("Sólo se puede insertar strings")

    return len(texto.replace(" ", ""))


try:
    print(caracteres_totales("Estoy haciendo el ejercicio número 25 de Python"))
except TypeError as e:
    print(f"Error: {e}")