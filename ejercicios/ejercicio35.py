# Ejercicio 35
#
# Crea la clase UsuarioBanco
#
# - Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# - Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
# - Código a seguir:
#     a. Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
#     b. Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
#     c. Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
#     d. Implementar agregar_dinero para aumentar el saldo del usuario.
#
# - Caso de uso:
#     a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#     b. Agregar 20 unidades al saldo de Bob.
#     c. Transferir 80 unidades de Bob a Alicia.
#     d. Retirar 50 unidades del saldo de Alicia.


# Escribe tu solución aquí

class UsuarioBanco:

    def __init__(self, nombre, saldo, tiene_cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta = tiene_cuenta

    # No los piden el ejercicio, pero me parece buena práctica
    def _comprobar_cuenta(self):
        if not self.tiene_cuenta:
            raise ValueError("El usuario no tiene cuenta corriente")

    def _comprobar_importe(self, importe):
        if importe <= 0:
            raise ValueError("El importe debe ser mayor que 0")


    def retirar_dinero(self, importe):

        self._comprobar_cuenta()
        self._comprobar_importe(importe)
        if self.saldo < importe:
            raise ValueError("No puedes retirar una cantidad mayor a tu saldo")

        self.saldo -= importe

    def transferir_dinero(self, otro, importe):
        """Transfiere dinero desde self (quien envía) hacia otro (quien recibe)."""

        self._comprobar_cuenta()
        otro._comprobar_cuenta()
        self._comprobar_importe(importe)

        if self.saldo < importe:
            raise ValueError("No puedes transferir una cantidad mayor a tu saldo")

        self.saldo -= importe
        otro.saldo += importe

    def agregar_dinero(self, importe):

        self._comprobar_cuenta()
        self._comprobar_importe(importe)
        
        self.saldo += importe

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

try:
    bob.agregar_dinero(20)
except ValueError as e:
    print(f"Error: {e}")

try:
    bob.transferir_dinero(alicia, 80)
except ValueError as e:
    print(f"Error: {e}")

try:
    alicia.retirar_dinero(50)
except ValueError as e:
    print(f"Error: {e}")

print(f"Saldo de Alicia: {alicia.saldo}")
print(f"Saldo de Bob: {bob.saldo}")
