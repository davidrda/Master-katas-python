# Ejercicio 34
#
# Crea la clase Arbol
#
# - Define un árbol genérico con un tronco y ramas como atributos.
# - Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
# - Código a seguir:
#     a. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#     b. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#     c. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#     d. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#     e. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#     f. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
#
# - Caso de uso:
#     a. Crear un árbol.
#     b. Hacer crecer el tronco una unidad.
#     c. Añadir una nueva rama.
#     d. Hacer crecer todas las ramas una unidad.
#     e. Añadir dos nuevas ramas.
#     f. Retirar la rama situada en la posición 2.
#     g. Obtener información sobre el árbol.


# Escribe tu solución aquí

class Arbol:

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    def quitar_rama(self, posicion):
        if posicion >= len(self.ramas):
            raise IndexError("No existe esta posición")
        
        if posicion < 0 or posicion >= len(self.ramas):
            raise IndexError("No existe esta posición")
        
        return self.ramas.pop(posicion)

    def info_arbol(self):
        return f"Longitud del tronco: {self.tronco} - Número de ramas: {len(self.ramas)} y sus longitudes: {self.ramas}"
        

arbol = Arbol()

arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()

try:
    arbol.quitar_rama(2)
except IndexError as e:
    print(f"Error: {e}")

print(arbol.info_arbol())


