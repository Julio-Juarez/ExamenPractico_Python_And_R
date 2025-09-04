# Creo una lista con la información del empleado
empleado <- list(
  nombre = "Carlos Pérez",             # cadena de texto
  salario = 4500,                      # número (salario mensual)
  horas = c(7, 9, 8)                   # vector con horas trabajadas en 3 días
)

# Imprimo el salario usando el operador $
empleado$salario   # acceso directo al campo "salario"

# Actualizo las horas trabajadas del segundo día a un nuevo valor (por ejemplo 10 horas)
empleado$horas[2] <- 10   # modifico el segundo elemento del vector dentro de la lista

# Agrego una nueva entrada llamada "departamento" con un valor de texto
empleado$departamento <- "Recursos Humanos"  # se añade una nueva clave-valor a la lista

# Imprimo los nombres de las entradas de la lista
names(empleado)   # muestra "nombre", "salario", "horas", "departamento"

# Filtro e imprimo las horas trabajadas mayores a 8
empleado$horas[empleado$horas > 8]   # condición lógica para filtrar los valores del vector horas

