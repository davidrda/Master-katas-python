# Ejercicio 32
#
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.


# Escribe tu solución aquí

empleados = [
    {"nombre": "Ana Pérez", "puesto": "Directora"},
    {"nombre": "Luis García", "puesto": "Desarrollador backend"},
    {"nombre": "Marta Ruiz", "puesto": "Diseñadora UX"},
    {"nombre": "Carlos Soler", "puesto": "Administrador de sistemas"},
    {"nombre": "Lucía Fernández", "puesto": "Analista de datos"},
]

def buscar_empleado(nombre, lista_empleados):

    nombre_normalizado = nombre.strip().lower()

    for empleado in lista_empleados:

        if nombre_normalizado == empleado["nombre"].strip().lower():
            return empleado["puesto"]
        
    return f"El nombre {nombre} no figura en la lista de empleados"


print(buscar_empleado("carlos soler", empleados))
print(buscar_empleado("Paquito el chocolatero", empleados))
