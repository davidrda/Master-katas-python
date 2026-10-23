# Ejercicio 20
#
# Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().


# Escribe tu solución aquí

lista = [25, "hola", "adios", 748, 384, 471, "ok", 1]

lista_int = list(filter(lambda i: type(i) == int, lista))

print(lista_int)