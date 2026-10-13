# Ejercicio 1
#
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.


# Escribe tu solución aquí

def contar_frecuencias(texto):

    texto_nuevo = texto.lower()
    frecuencias = {}

    for letra in texto_nuevo:

        if letra == " " :
            continue

        if letra not in frecuencias:
            frecuencias[letra] = 1
        else:
            frecuencias[letra] += 1


    return frecuencias


texto = input("Inserta el texto:")

print(contar_frecuencias(texto))
