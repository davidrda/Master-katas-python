# Ejercicio 31
#
# Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.


# Escribe tu solución aquí

def buscar_nombre():

    nombres = input("Introduce los nombres de la lista: ")

    if not nombres.strip():
        raise ValueError("No se puede introducir una lista vacía")

    lista_nombres = [nombre.strip().lower() for nombre in nombres.split(",")]

    nombre_a_buscar = input("Introduce el nombre a buscar: ").strip().lower()


    if nombre_a_buscar in lista_nombres:
        print(f"¡Nombre {nombre_a_buscar} encontrado!")
    else:
        raise ValueError(f"No se ha encontrado el nombre {nombre_a_buscar}")
    

try:
    buscar_nombre()
except ValueError as e:
    print(f"Error: {e}")


