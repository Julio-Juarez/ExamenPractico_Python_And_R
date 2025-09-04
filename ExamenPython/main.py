
# ============================================
# PROGRAMA DE GESTIÓN DE EMPLEADOS DE AGENCIAS
# ============================================
# Este programa permite registrar empleados, listarlos, filtrarlos, actualizarlos,
# eliminarlos y generar resúmenes salariales. 
# Todo se maneja con un menú interactivo basado en opciones numéricas.

# -------------------------------
# LISTAS Y CONSTANTES NECESARIAS
# -------------------------------

# Lista vacía para almacenar a todos los empleados
# Cada empleado será un diccionario con: nombre, puesto, sueldo y agencia
empleados = []

# Puestos válidos permitidos en el sistema
puestos_validos = ["Cajero", "Ejecutivo de Cuenta", "Gerente de Agencia"]

# Agencias válidas permitidas en el sistema
agencias_validas = ["Agencia Central Zona 1", "Agencia Roosevelt", "Agencia Quetzaltenango"]

# Sueldo mínimo permitido para cualquier empleado
SUELDO_MINIMO = 3000


# -------------------------------
# FUNCIÓN: Registrar empleado
# -------------------------------
def registrar_empleado():
    """Función para registrar un nuevo empleado en el sistema"""
    print("\n--- Registrar Empleado ---")
    
    # Pedimos el nombre del empleado
    nombre = input("Ingrese el nombre del empleado: ")
    
    # Validamos que el puesto ingresado esté en la lista de puestos válidos
    print("\nSeleccione el puesto:")
    # Mostramos los puestos disponibles numerados
    for i, puesto in enumerate(puestos_validos, start=1):
        print(f"{i}. {puesto}")

    # Ciclo para asegurar que se ingrese una opción válida
    while True:
        opcion_puesto = input("Digite el número del puesto: ")
        # Verificamos si la opción es un número y está en el rango correcto
        if opcion_puesto.isdigit() and 1 <= int(opcion_puesto) <= len(puestos_validos):
            puesto = puestos_validos[int(opcion_puesto) - 1]  # Obtenemos el puesto seleccionado
            break  # Salimos del ciclo while
        else:
            print("Opción inválida. Intente de nuevo.")
    
    # Validamos que el sueldo sea mayor al mínimo permitido
    while True:
        try:
            # Intentamos convertir el input a número decimal
            sueldo = float(input("Ingrese el sueldo (mínimo Q3,000): Q"))
            if sueldo > SUELDO_MINIMO:   # Verificamos que sea mayor al mínimo
                break  # Salimos del ciclo si es válido
            else:
                print("El sueldo debe ser mayor a Q3,000.")
        except ValueError:  # Capturamos error si no se ingresa un número
            print("Debe ingresar un número válido.")
    
    # Validamos que la agencia ingresada sea una de las permitidas
    print("\nSeleccione la agencia:")
    # Mostramos las agencias disponibles numeradas
    for i, agencia in enumerate(agencias_validas, start=1):
        print(f"{i}. {agencia}")

    # Ciclo para asegurar que se ingrese una opción válida
    while True:
        opcion_agencia = input("Digite el número de la agencia: ")
        # Verificamos si la opción es un número y está en el rango correcto
        if opcion_agencia.isdigit() and 1 <= int(opcion_agencia) <= len(agencias_validas):
            agencia = agencias_validas[int(opcion_agencia) - 1]  # Obtenemos la agencia seleccionada
            break  # Salimos del ciclo while
        else:
            print("Opción inválida. Intente de nuevo.")
    
    # Creamos un diccionario con los datos del empleado
    empleado = {
        "nombre": nombre, 
        "puesto": puesto, 
        "sueldo": sueldo, 
        "agencia": agencia
    }
    
    # Agregamos el empleado a la lista principal
    empleados.append(empleado)
    
    print("Empleado registrado con éxito.")


# -------------------------------
# FUNCIÓN: Mostrar todos los empleados
# -------------------------------
def mostrar_empleados():
    """Función para mostrar todos los empleados registrados"""
    print("\n--- Lista de Empleados ---")
    
    # Verificamos si hay empleados registrados
    if not empleados:
        print("No hay empleados registrados.")
        return  # Salimos de la función si no hay empleados
    
    # Recorremos la lista de empleados y mostramos cada uno con un número
    for i, emp in enumerate(empleados, start=1):
        print(f"{i}. {emp['nombre']} - {emp['puesto']} - Q{emp['sueldo']} - {emp['agencia']}")


# -------------------------------
# FUNCIÓN: Filtrar empleados por agencia
# -------------------------------
def filtrar_por_agencia():
    """Función para filtrar y mostrar empleados por agencia"""
    print("\n--- Filtrar por Agencia ---")
    print("Seleccione la agencia para filtrar:")
    
    # Mostramos las agencias disponibles numeradas
    for i, agencia in enumerate(agencias_validas, start=1):
        print(f"{i}. {agencia}")

    # Ciclo para asegurar que se ingrese una opción válida
    while True:
        opcion_agencia = input("Digite el número de la agencia: ")
        # Verificamos si la opción es un número y está en el rango correcto
        if opcion_agencia.isdigit() and 1 <= int(opcion_agencia) <= len(agencias_validas):
            agencia = agencias_validas[int(opcion_agencia) - 1]  # Obtenemos la agencia seleccionada
            break  # Salimos del ciclo while
        else:
            print("Opción inválida. Intente de nuevo.")

    # Filtramos empleados por la agencia seleccionada
    # Usamos list comprehension para crear una lista solo con los empleados de esa agencia
    filtrados = [emp for emp in empleados if emp["agencia"] == agencia]

    # Verificamos si hay empleados en la agencia seleccionada
    if not filtrados:
        print(f"No hay empleados registrados en la agencia {agencia}.")
    else:
        # Mostramos los empleados filtrados
        print(f"\nEmpleados en la agencia {agencia}:")
        for emp in filtrados:
            print(f"- {emp['nombre']} | Puesto: {emp['puesto']} | Sueldo: Q{emp['sueldo']}")


# -------------------------------
# FUNCIÓN: Actualizar información de un empleado
# -------------------------------
def actualizar_empleado():
    """Función para actualizar información de un empleado existente"""
    print("\n--- Actualizar Empleado ---")
    # Mostramos todos los empleados para que el usuario pueda seleccionar
    mostrar_empleados()
    
    # Verificamos si hay empleados registrados
    if not empleados:
        return  # Salimos de la función si no hay empleados
    
    try:
        # Solicitamos el número del empleado a actualizar
        indice = int(input("Seleccione el número de empleado a actualizar: ")) - 1
        
        # Verificamos que el índice esté dentro del rango válido
        if 0 <= indice < len(empleados):
            emp = empleados[indice]  # Obtenemos el empleado seleccionado
            print(f"Empleado seleccionado: {emp['nombre']}")
            
            # Submenú de actualización
            opcion = input("¿Qué desea actualizar? (1: Sueldo, 2: Agencia): ")
            
            # Actualización de sueldo
            if opcion == "1":
                while True:
                    try:
                        nuevo_sueldo = float(input("Ingrese el nuevo sueldo: Q"))
                        if nuevo_sueldo > SUELDO_MINIMO:  # Validamos que sea mayor al mínimo
                            emp["sueldo"] = nuevo_sueldo  # Actualizamos el sueldo
                            print("Sueldo actualizado con éxito.")
                            break  # Salimos del ciclo
                        else:
                            print("El sueldo debe ser mayor a Q3,000.")
                    except ValueError:  # Capturamos error si no se ingresa un número
                        print("Debe ingresar un número válido.")
            
            # Actualización de agencia        
            elif opcion == "2":
                while True:
                    nueva_agencia = input(f"Ingrese la nueva agencia, coloquela Textualmente ({agencias_validas}): ")
                    if nueva_agencia in agencias_validas:  # Validamos que sea una agencia válida
                        emp["agencia"] = nueva_agencia  # Actualizamos la agencia
                        print("Agencia actualizada con éxito.")
                        break  # Salimos del ciclo
                    else:
                        print("Agencia no válida.")
            else:
                print("Opción no válida.")
        else:
            print("Empleado no encontrado.")
    except ValueError:  # Capturamos error si no se ingresa un número
        print("Debe ingresar un número válido.")


# -------------------------------
# FUNCIÓN: Eliminar empleado
# -------------------------------
def eliminar_empleado():
    """Función para eliminar un empleado del sistema"""
    print("\n--- Eliminar Empleado ---")
    # Mostramos todos los empleados para que el usuario pueda seleccionar
    mostrar_empleados()
    
    # Verificamos si hay empleados registrados
    if not empleados:
        return  # Salimos de la función si no hay empleados
    
    try:
        # Solicitamos el número del empleado a eliminar
        indice = int(input("Seleccione el número de empleado a eliminar: ")) - 1
        
        # Verificamos que el índice esté dentro del rango válido
        if 0 <= indice < len(empleados):
            # Eliminamos el empleado usando pop (que también nos devuelve el elemento eliminado)
            eliminado = empleados.pop(indice)
            print(f"Empleado {eliminado['nombre']} eliminado con éxito.")
        else:
            print("Empleado no encontrado.")
    except ValueError:  # Capturamos error si no se ingresa un número
        print("Debe ingresar un número válido.")


# -------------------------------
# FUNCIÓN: Resumen salarial
# -------------------------------
def resumen_salarial():
    """Función para generar un resumen de los salarios por agencia y puesto"""
    print("\n--- Resumen Salarial ---")
    
    # Verificamos si hay empleados registrados
    if not empleados:
        print("No hay empleados registrados.")
        return  # Salimos de la función si no hay empleados
    
    # Obtenemos todos los sueldos en una lista
    sueldos = [emp["sueldo"] for emp in empleados]
    
    # Calculamos el total y promedio general
    total = sum(sueldos)
    promedio = total / len(sueldos)
    
    print(f"Sueldo total general: Q{total}")
    print(f"Promedio general: Q{promedio:.2f}")  # Formateamos a 2 decimales
    
    # Resumen por agencia
    print("\nPor agencia:")
    for agencia in agencias_validas:
        # Filtramos sueldos por agencia
        sueldos_agencia = [emp["sueldo"] for emp in empleados if emp["agencia"] == agencia]
        
        # Solo mostramos si hay empleados en esta agencia
        if sueldos_agencia:
            total_agencia = sum(sueldos_agencia)
            promedio_agencia = total_agencia / len(sueldos_agencia)
            print(f"{agencia} - Total: Q{total_agencia}, Promedio: Q{promedio_agencia:.2f}")
    
    # Resumen por puesto
    print("\nPor puesto:")
    for puesto in puestos_validos:
        # Filtramos sueldos por puesto
        sueldos_puesto = [emp["sueldo"] for emp in empleados if emp["puesto"] == puesto]
        
        # Solo mostramos si hay empleados en este puesto
        if sueldos_puesto:
            total_puesto = sum(sueldos_puesto)
            promedio_puesto = total_puesto / len(sueldos_puesto)
            print(f"{puesto} - Total: Q{total_puesto}, Promedio: Q{promedio_puesto:.2f}")


# -------------------------------
# MENÚ PRINCIPAL
# -------------------------------
def menu():
    """Función principal que muestra el menú y gestiona las opciones"""
    # Ciclo infinito hasta que el usuario elija salir
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar empleado")
        print("2. Mostrar todos los empleados")
        print("3. Filtrar empleados por agencia")
        print("4. Actualizar información de un empleado")
        print("5. Eliminar empleado")
        print("6. Resumen salarial")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        # Ejecutamos la función correspondiente a la opción seleccionada
        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            filtrar_por_agencia()
        elif opcion == "4":
            actualizar_empleado()
        elif opcion == "5":
            eliminar_empleado()
        elif opcion == "6":
            resumen_salarial()
        elif opcion == "7":
            print("Saliendo del programa...")
            break  # Rompemos el ciclo while para salir del programa
        else:
            print("Opción no válida. Intente de nuevo.")


# -------------------------------
# EJECUCIÓN DEL PROGRAMA
# -------------------------------
# Esta línea asegura que el menú solo se ejecute cuando el archivo es run directamente
# y no cuando es importado como módulo
if __name__ == "__main__":
    menu()