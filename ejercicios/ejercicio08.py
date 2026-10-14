# Ejercicio 8
#
# Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.


# Escribe tu solución aquí


try:
    num1 = float(input("Introduce el número 1: "))
    num2 = float(input("Introduce el número 2: "))
    resultado = num1 / num2
except ValueError:
    print("Debes introducir un número")
except ZeroDivisionError:
    print("No puedes dividir entre 0")
else:
    print(f'La división entre {num1} y {num2} es: {resultado}')





