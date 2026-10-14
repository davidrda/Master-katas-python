# Ejercicio 9
#
# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().


# Escribe tu solución aquí

MASCOTAS_PROHIBIDAS = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

def lista_exclusion_mascotas(lista):

    excluidas = list(map(str.lower, MASCOTAS_PROHIBIDAS))

    lista_minusculas = list(map(str.lower, lista))

    lista_definitiva = list(filter(lambda l: l not in excluidas, lista_minusculas))

    return lista_definitiva

lista = ["Perro", "Gato", "Tigre", "Pez", "Oso", "Agaporni", "oso", "TORTUGA"]

print(lista_exclusion_mascotas(lista))
