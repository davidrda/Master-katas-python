# Ejercicio 3
#
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.


# Escribe tu solución aquí

lista_palabras = ["Hola", "Hola mundo", "Adios", "Hasta mañana!", "Nos vemos mañana!"]

def palabras_objetivo(lista, objetivo):

    lista_palabras_objetivo = []

    for palabra in lista:

        if objetivo in palabra:

            lista_palabras_objetivo.append(palabra)

    return lista_palabras_objetivo

print(palabras_objetivo(lista_palabras, "Hola"))