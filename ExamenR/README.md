# Manual Teórico-Práctico de R

---

## 1. Variables y Operaciones

### Teoría
- **Variable:** espacio de memoria que almacena un valor.  
- **Tipos de datos básicos en R:**
  - `numeric` → números (enteros o decimales)  
  - `character` → texto  
  - `logical` → TRUE/FALSE  
- **Conversión de tipos:** `as.character()`, `as.numeric()`, etc.  
- **Concatenación de cadenas:** `paste()` une texto y variables.  
- **Operadores matemáticos:**
  - `+`, `-`, `*`, `/` → suma, resta, multiplicación, división  
  - `^` → potencia

### Ejemplo aplicado

```r
# Creo una variable numérica
num <- 4

# Convierto la variable a tipo carácter
num_text <- as.character(num)

# Concateno con una frase usando paste()
frase <- paste("Valor:", num_text)

# Imprimo el tipo de dato de la variable concatenada
class(frase)

# Calculo el cubo del número original
cubo <- num^3
cubo
```

---

## 2. Vectores

### Teoría
- **Vector:** estructura que almacena múltiples elementos del mismo tipo.  
- **Funciones útiles:**
  - `c()` → combina valores en un vector  
  - `names()` → asigna o consulta nombres de elementos  
  - `length()` → obtiene el tamaño del vector  
  - `sum()` → suma todos los elementos  
- **Filtrado:** usando condiciones lógicas dentro de corchetes `[ ]`.

### Ejemplo aplicado

```r
# Creo un vector con 5 calificaciones
califs <- c(78, 85, 92, 60, 73)

# Asigno nombres a cada calificación
names(califs) <- c("Examen1", "Examen2", "Examen3", "Examen4", "Examen5")

# Imprimo la calificación del tercer examen
califs["Examen3"]

# Actualizo la calificación del primer examen sumando 5
califs["Examen1"] <- califs["Examen1"] + 5

# Filtrar calificaciones mayores a 70
califs[califs > 70]

# Calcular promedio usando sum() y length()
promedio <- sum(califs) / length(califs)
promedio
```

---

## 3. Listas

### Teoría
- **Lista:** estructura que puede contener distintos tipos de datos (números, texto, vectores, etc.).  
- **Funciones y operadores:**
  - `list()` → crea una lista  
  - `$` → accede a un elemento de la lista por nombre  
  - `names()` → obtiene o asigna nombres de elementos en la lista  
  - Filtrado usando corchetes `[ ]` y condiciones

### Ejemplo aplicado

```r
# Creo una lista con información de un empleado
empleado <- list(
  nombre = "Carlos Pérez",
  salario = 4500,
  horas = c(7, 9, 8)
)

# Imprimo el salario usando $
empleado$salario

# Actualizo las horas trabajadas del segundo día
empleado$horas[2] <- 10

# Agrego una nueva entrada "departamento"
empleado$departamento <- "Recursos Humanos"

# Imprimo los nombres de las entradas
names(empleado)

# Filtrar horas mayores a 8
empleado$horas[empleado$horas > 8]
```

---

## 4. Data Frames y Archivos

### Teoría
- **Data frame:** estructura tipo tabla con filas y columnas, cada columna puede tener distinto tipo de dato.  
- **Funciones clave:**
  - `data.frame()` → crea un data frame  
  - `$` → accede a una columna  
  - `summary()` → resumen estadístico por columna  
  - `write.csv()` → guarda data frames en CSV  
- **Manipulación:**
  - Modificar elementos: `df$columna[fila] <- valor`  
  - Eliminar filas: `df <- df[-fila, ]`

### Ejemplo aplicado

```r
# Creo un data frame con 3 productos
productos <- data.frame(
  nombre = c("Laptop", "Teléfono", "Tablet"),
  precio = c(5000, 2500, 1500),
  disponible = c(TRUE, FALSE, TRUE)
)

# Imprimo la columna de precios
productos$precio

# Actualizo el precio del segundo producto
productos$precio[2] <- productos$precio[2] + 100

# Elimino la tercera fila
productos <- productos[-3, ]

# Guardo el data frame en un CSV sin índices
write.csv(productos, "productos.csv", row.names = FALSE)

# Imprimo un resumen del data frame
summary(productos)
```

---

## 5. Estructuras de Control y Funciones

### Teoría
- **Funciones:** bloques de código reutilizables  
  - `function()` → define una función  
  - `return()` → devuelve un valor
- **Bucles y condicionales:**
  - `for()` → iteración  
  - `if-else` → toma de decisiones según condiciones
- **Operadores de comparación:** `>`, `<`, `>=`, `<=`, `==`, `!=`

### Ejemplo aplicado

```r
# Defino la función calcular_total que suma un vector
calcular_total <- function(vec) {
  total <- sum(vec)
  return(total)
}

# Creo un vector de ejemplo
mis_numeros <- c(5, 8, 12, 3)

# Uso la función para calcular la suma
resultado <- calcular_total(mis_numeros)
resultado

# Bucle for para recorrer números del 1 al 6
for (i in 1:6) {
  if (i > 4) {
    print(paste(i, "es mayor que 4"))
  } else {
    print(paste(i, "es menor o igual a 4"))
  }
}
```

---

## Conclusión
Este manual cubre los conceptos básicos de **R**:

1. Variables, tipos y operaciones  
2. Vectores y operaciones con nombres y filtros  
3. Listas y manipulación de datos heterogéneos  
4. Data frames y manejo de archivos CSV  
5. Funciones, bucles y condicionales  

Estos son los fundamentos para **programar y analizar datos en R**.
