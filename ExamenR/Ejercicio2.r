# Crear un vector con las calificaciones de 5 exámenes
calificaciones <- c(65, 78, 90, 55, 82)   # Vector con valores numéricos entre 0 y 100

# Asignar nombres a cada elemento del vector
names(calificaciones) <- c("Examen1", "Examen2", "Examen3", "Examen4", "Examen5")

# Seleccionar e imprimir la calificación del tercer examen
print(paste("La calificación del tercer examen es:", calificaciones["Examen3"]))

# Actualizar la calificación del primer examen sumándole 5 puntos
calificaciones["Examen1"] <- calificaciones["Examen1"] + 5

# Filtrar e imprimir las calificaciones mayores a 70
mayores_70 <- calificaciones[calificaciones > 70]   # Filtramos solo las notas > 70
print("Las calificaciones mayores a 70 son:")
print(mayores_70)

# Calcular e imprimir el promedio de las calificaciones usando sum() y length()
promedio <- sum(calificaciones) / length(calificaciones)
print(paste("El promedio de las calificaciones es:", promedio))
