# Ejercicio 30
#
# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.


# Escribe tu solución aquí

def son_anagramas(p1, p2):

    if not isinstance(p1, str) or not isinstance(p2, str):
        raise ValueError("Las dos palabras deben de ser texto")

    # .strip() elimina los espacios de los lados, si está vacio cuenta como False
    if not p1.strip() or not p2.strip():
        raise ValueError("Las palabras no pueden estar vacias")

    return sorted(p1.lower()) == sorted(p2.lower())

try:
    if son_anagramas("Roma", "Amor"):
        print("¡Son anagramas! :)")
    else:
        print("No son anagramas :(")
except ValueError as e:
    print(f"Error: {e}")
    

