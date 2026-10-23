# Ejercicio 29
#
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.


# Escribe tu solución aquí

def enmascarar(variable):

    variable_string = str(variable)

    parte_oculta = variable_string[:-4]
    parte_visible = variable_string[-4:]

    parte_enmascarada = "#" * len(parte_oculta)

    return parte_enmascarada + parte_visible


x = 848728299383

print(enmascarar(x))