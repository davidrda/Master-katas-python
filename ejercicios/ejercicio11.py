# Ejercicio 11
#
# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.


# Escribe tu solución aquí

EDAD_MINIMA = 0
EDAD_MAXIMA = 120


def validar_edad(texto):
    try:
        edad = int(texto)
    except ValueError:
        raise ValueError("Tienes que insertar un número entero") from None

    if not EDAD_MINIMA <= edad <= EDAD_MAXIMA:
        raise ValueError(f"La edad debe estar entre {EDAD_MINIMA} y {EDAD_MAXIMA}")

    return edad


while True:
    try:
        edad = validar_edad(input("Escribe tu edad: "))
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Edad registrada: {edad}")
        break