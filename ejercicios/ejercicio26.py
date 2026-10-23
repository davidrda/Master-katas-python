# Ejercicio 26
#
# Crea una función lambda que calcule el resto de la división entre dos números dados.


# Escribe tu solución aquí

num1 = 8
num2 = 4

resto = lambda n1, n2: n1 % n2

try:
    print(resto(num1, num2))
except ZeroDivisionError:
    print("Error: no se puede calcular el resto de una división entre 0")