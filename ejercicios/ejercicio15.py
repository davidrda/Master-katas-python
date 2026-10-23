# Ejercicio 15
#
# Crea una función lambda que sume 3 a cada número de una lista dada.


# Escribe tu solución aquí

lista = [7, 17, 22, 10, "Hola"]

lista_definitiva = list(
    map(lambda n: n + 3, 
        filter(lambda n: isinstance(n, int),lista ))) # Evito strings con el filter()

print(lista_definitiva)
