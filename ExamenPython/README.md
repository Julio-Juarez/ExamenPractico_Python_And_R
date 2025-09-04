# 📘 Manual Teórico: Sistema de Gestión de Empleados en Python

## 📋 Tabla de Contenidos
1. [Introducción](#introducción)
2. [Estructura del Programa](#estructura-del-programa)
3. [Palabras Reservadas](#palabras-reservadas)
4. [Funciones Integradas](#funciones-integradas)
5. [Funciones Personalizadas](#funciones-personalizadas)
6. [Estructuras de Datos](#estructuras-de-datos)
7. [Comprensión de Listas](#comprensión-de-listas)
8. [Control de Flujo](#control-de-flujo)
9. [Manejo de Errores](#manejo-de-errores)
10. [Ejecución del Programa](#ejecución-del-programa)
11. [Conceptos Clave](#conceptos-clave)

---

## 🎯 Introducción
Este programa es un sistema de gestión de empleados para agencias que permite:

- Registrar nuevos empleados  
- Listar empleados existentes  
- Filtrar empleados por agencia  
- Actualizar información de empleados  
- Eliminar empleados  
- Generar resúmenes salariales

Este sistema está diseñado para **practicar conceptos de programación estructurada y orientada a objetos**, manejo de datos y control de flujo.

---

## 🏗️ Estructura del Programa

### Comentarios y Documentación
```python
# ============================================
# PROGRAMA DE GESTIÓN DE EMPLEADOS DE AGENCIAS
# ============================================
```
- Los comentarios se indican con `#` y permiten **documentar el código**, facilitando su comprensión y mantenimiento.

### Variables Globales y Constantes
```python
empleados = []  # Lista para almacenar empleados
puestos_validos = ["Cajero", "Ejecutivo de Cuenta", "Gerente de Agencia"]
agencias_validas = ["Agencia Central Zona 1", "Agencia Roosevelt", "Agencia Quetzaltenango"]
SUELDO_MINIMO = 3000  # Constante en mayúsculas (convención)
```
- Se recomienda usar **mayúsculas para constantes** por convención.

---

## 🔑 Palabras Reservadas

### `def`
Define una función:
```python
def registrar_empleado():
    """Función para registrar un nuevo empleado"""
```

### `if/elif/else`
Estructuras condicionales:
```python
if opcion == "1":
    registrar_empleado()
elif opcion == "2":
    mostrar_empleados()
else:
    print("Opción no válida")
```

### `while`
Bucle que se ejecuta mientras se cumpla una condición:
```python
while True:  # Bucle infinito
    # código del menú
```

### `for`
Bucle que itera sobre elementos:
```python
for i, puesto in enumerate(puestos_validos, start=1):
    print(f"{i}. {puesto}")
```

### `try/except`
Manejo de excepciones:
```python
try:
    sueldo = float(input("Ingrese el sueldo: Q"))
except ValueError:
    print("Debe ingresar un número válido")
```

### `return`
Devuelve un valor de una función:
```python
return  # Sale de la función sin valor
```

### `break`
Sale de un bucle anticipadamente:
```python
break  # Termina el bucle while
```

### `in`
Comprueba pertenencia:
```python
if nueva_agencia in agencias_validas:
```

---

## 🛠️ Funciones Integradas

- `print()`: Muestra texto en la consola
```python
print("Texto a mostrar")
```
- `input()`: Lee entrada del usuario
```python
nombre = input("Ingrese el nombre: ")
```
- `int()`: Convierte a entero
```python
numero = int("5")  # Resultado: 5
```
- `float()`: Convierte a decimal
```python
decimal = float("3.14")  # Resultado: 3.14
```
- `enumerate()`: Devuelve índice y elemento
```python
for i, valor in enumerate(lista, start=1):
```
- `isdigit()`: Verifica si es dígito
```python
if opcion.isdigit():
```
- `sum()`: Suma elementos
```python
total = sum([1, 2, 3])  # Resultado: 6
```
- `len()`: Longitud de secuencia
```python
cantidad = len(empleados)  # Número de empleados
```

---

## 📋 Funciones Personalizadas

- `registrar_empleado()`: Registra un nuevo empleado con validación de datos.  
- `mostrar_empleados()`: Muestra todos los empleados registrados.  
- `filtrar_por_agencia()`: Filtra empleados por agencia seleccionada.  
- `actualizar_empleado()`: Actualiza información de empleados existentes.  
- `eliminar_empleado()`: Elimina empleados del sistema.  
- `resumen_salarial()`: Genera reportes de salarios por agencia y puesto.  
- `menu()`: Función principal con menú interactivo.

---

## 🗃️ Estructuras de Datos

### Listas
```python
empleados = []  # Lista vacía
puestos_validos = ["Cajero", "Ejecutivo de Cuenta", "Gerente de Agencia"]
```
- Permiten almacenar **colecciones de elementos ordenados**.

### Diccionarios
Cada empleado se representa como:
```python
empleado = {
    "nombre": "Juan Pérez",
    "puesto": "Cajero",
    "sueldo": 3500.50,
    "agencia": "Agencia Central Zona 1"
}
```
- Los diccionarios permiten **almacenar datos clave-valor**, ideales para representar entidades como empleados.

### Comprensión de Listas
```python
filtrados = [emp for emp in empleados if emp["agencia"] == agencia]
```
- Permite **crear listas nuevas** a partir de listas existentes aplicando condiciones o transformaciones.
- Más eficiente y legible que un bucle `for` clásico.

# 🔹 Comprensión de Listas (list comprehension)

La comprensión de listas es una forma **compacta y elegante** de crear nuevas listas a partir de listas existentes (u otras secuencias), aplicando condiciones y/o operaciones a cada elemento.

## Estructura básica
```python
[nueva_expresion for elemento in secuencia if condicion]
```
- `nueva_expresion` → Qué valor queremos que tenga cada elemento de la nueva lista.
- `elemento` → Cada elemento de la lista original o secuencia.
- `secuencia` → Lista o iterador del que queremos generar la nueva lista.
- `if condicion` → (Opcional) Filtra elementos según una condición booleana.

## 🔹 Ejemplo 1: Lista simple de cuadrados
```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)
```
**Salida:**
```
[1, 4, 9, 16, 25]
```
Aquí, `x**2` es la nueva expresión aplicada a cada elemento `x` de `numeros`.

## 🔹 Ejemplo 2: Filtrado con condición
```python
numeros = [1, 2, 3, 4, 5]
pares = [x for x in numeros if x % 2 == 0]
print(pares)
```
**Salida:**
```
[2, 4]
```
Solo se incluyen los números pares (`x % 2 == 0`).

## 🔹 Ejemplo 3: Aplicación práctica con empleados
```python
empleados = [
    {"nombre": "Juan", "agencia": "Central"},
    {"nombre": "Ana", "agencia": "Roosevelt"},
    {"nombre": "Luis", "agencia": "Central"}
]

# Filtrar empleados de la agencia "Central"
filtrados = [emp for emp in empleados if emp["agencia"] == "Central"]
print(filtrados)
```
**Salida:**
```
[{'nombre': 'Juan', 'agencia': 'Central'}, {'nombre': 'Luis', 'agencia': 'Central'}]
```
- `emp` → cada diccionario de `empleados`
- `emp["agencia"] == "Central"` → condición para filtrar
- `[emp for ...]` → crea una **nueva lista** solo con los empleados que cumplen la condición

## 🔹 Ventajas de la comprensión de listas
- **Código más corto**: reemplaza varios bucles `for` con pocas líneas.
- **Más legible**: todo está en una sola línea (si no es demasiado larga).
- **Flexible**: puedes aplicar operaciones, filtros y combinaciones.

#### Ejemplo avanzado
```python
# Lista de nombres de empleados de la agencia Central con sueldo > 3000
nombres_filtrados = [emp["nombre"] for emp in empleados if emp["agencia"] == "Central" and emp["sueldo"] > 3000]
```
- Combina **múltiples condiciones** y transforma elementos directamente.

---

## 🔄 Control de Flujo

### Validación de Entrada
```python
while True:
    opcion = input("Seleccione opción: ")
    if opcion.isdigit() and 1 <= int(opcion) <= 7:
        break
    print("Opción inválida")
```

### Menú Interactivo
```python
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar empleado")
        print("2. Mostrar empleados")
        # ... más opciones
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        # Procesar opción
```

- Permite al usuario **interactuar con el sistema** y elegir acciones.

---

## ⚠️ Manejo de Errores

### Validación de Tipos
```python
try:
    valor = float(input("Ingrese un número: "))
except ValueError:
    print("Error: Debe ingresar un número válido")
```

### Validación de Rango
```python
if 0 <= indice < len(empleados):
    # Índice válido
else:
    print("Índice fuera de rango")
```
- Evita que el programa **falle por entradas incorrectas**.

---

## 🚀 Ejecución del Programa

### Bloque Principal
```python
if __name__ == "__main__":
    menu()
```
- Permite que el código del menú se ejecute solo si el archivo es ejecutado directamente, no cuando es importado.

---

## 💡 Conceptos Clave

- **Modularización**: Código organizado en funciones especializadas.  
- **Validación**: Verificación exhaustiva de entradas de usuario.  
- **Manejo de Errores**: Prevención de fallos con `try/except`.  
- **Interfaz de Usuario**: Menú interactivo basado en texto.  
- **Estructuras de Datos**: Uso de listas y diccionarios para almacenamiento.  
- **Comprensión de Listas**: Permite crear listas nuevas de manera eficiente con condiciones y transformaciones.

Este manual cubre todos los aspectos teóricos del sistema de gestión de empleados, incluyendo **palabras reservadas, funciones integradas, estructuras de control y conceptos de programación aplicados**.

