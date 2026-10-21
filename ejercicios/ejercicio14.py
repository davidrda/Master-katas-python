# Ejercicio 14
#
# Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().


# Escribe tu solución aquí

def palabras_letra_especifica(lista, letra):
    """Devuelve las palabras de la lista que empiezan por la letra dada,
    sin distinguir mayúsculas de minúsculas."""

    if not lista:
        raise ValueError("Inserta una lista con valores dentro")

    if len(letra) != 1:
        raise ValueError("Debes indicar una única letra")

    return list(filter(lambda p: (p.lower().startswith(letra.lower())),lista))


try:
    print(palabras_letra_especifica(["Adrian", "David", "Sergio", "Alberto"], "a"))
except ValueError as e:
    print(f"Error: {e}")
    
