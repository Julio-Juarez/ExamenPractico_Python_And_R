# Creo una función llamada calcular_total que recibe un vector numérico
calcular_total <- function(vec) {
  # vec es el vector de números que se pasa como argumento
  total <- sum(vec)   # sum() calcula la suma de todos los elementos del vector
  return(total)       # devuelve el resultado de la suma
}

# Creo un vector con 4 valores numéricos de ejemplo
mis_numeros <- c(5, 8, 12, 3)   # vector de 4 números

# Uso la función calcular_total para sumar los elementos del vector
resultado <- calcular_total(mis_numeros)  # llamo a la función y guardo el resultado
resultado  # imprimo el resultado en la consola

# Bucle for que recorre los números del 1 al 6
for (i in 1:6) {
  # if-else para verificar si el número es mayor o menor/igual a 4
  if (i > 4) {
    print(paste(i, "es mayor que 4"))   # imprime si el número es mayor que 4
  } else {
    print(paste(i, "es menor o igual a 4"))  # imprime si el número es menor o igual a 4
  }
}
