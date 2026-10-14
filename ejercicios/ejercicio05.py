# Ejercicio 5
#
# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.


# Escribe tu solución aquí
def calcular_media(lista, nota_aprobado = 5):

    if lista:
        suma = 0
        
        for numero in lista:
    
            suma += numero
    
        media = suma / len(lista)
    
        if media >= nota_aprobado:
            return (media, "aprobado")
        else:
            return (media, "suspenso")
        
    
    return None

lista_numeros = [5, 7, 2, 10, 4]

print(calcular_media(lista_numeros))

