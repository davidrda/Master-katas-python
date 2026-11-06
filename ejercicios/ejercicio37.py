# Ejercicio 37
#
# Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.


# Escribe tu solución aquí

def indicar_momento_del_dia(entrada):
    
    if not entrada.strip():
        raise ValueError("Inserta una hora")

    partes = entrada.split(":")

    if len(partes) > 2:
        raise ValueError("Formato no válido")

    try:
        hora = int(partes[0])
        minutos = int(partes[1]) if len(partes) == 2 else 0
    except ValueError:
        raise ValueError("Formato no válido")

    if hora < 0 or hora > 23 or minutos < 0 or minutos > 59:
        raise ValueError("Horario erróneo")

    if hora >= 22 or hora < 6:
        return "Es por la noche"

    if hora >= 14:
        return "Es por la tarde"

    return "Es por la mañana"


entrada = input("Indica la hora (HH:MM): ")

try:
    resultado = indicar_momento_del_dia(entrada)
    print(resultado)
except ValueError as e:
    print(f"Error: {e}")
