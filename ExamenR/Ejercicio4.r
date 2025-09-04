# Creo un data frame con información de 3 productos
productos <- data.frame(
  nombre = c("Laptop", "Teléfono", "Tablet"),  # columna de textos (nombres de productos)
  precio = c(5000, 2500, 1500),                # columna numérica (precios)
  disponible = c(TRUE, FALSE, TRUE)            # columna lógica (disponibilidad)
)

# Imprimo la columna de precios
productos$precio   # acceso directo a la columna "precio"

# Actualizo el precio del segundo producto sumándole 100
productos$precio[2] <- productos$precio[2] + 100   # modifico solo la segunda fila de precios

# Elimino la tercera fila del data frame
productos <- productos[-3, ]   # el signo "-" indica que elimino la fila 3

# Guardo el data frame en un archivo CSV llamado "productos.csv" sin índices de fila
write.csv(productos, "productos.csv", row.names = FALSE)  # row.names=FALSE evita guardar el índice

# Imprimo un resumen del data frame
summary(productos)   # summary() da estadísticas/resumen según el tipo de cada columna


