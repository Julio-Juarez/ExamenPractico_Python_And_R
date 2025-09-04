# Crear una variable que almacene un número entero
numero <- 5   # Asignamos el valor entero 5 a la variable 'numero'

# Convertir esa variable a tipo carácter (character)
numero_char <- as.character(numero)   # Usamos as.character() para convertir 'numero' en texto

# Concatenar una frase que incluya el valor de la variable usando paste()
frase <- paste("El valor almacenado es:", numero_char)   # Con paste() unimos texto y variable

# Imprimir el tipo de dato de la variable concatenada
print(typeof(frase))   # typeof() nos dice qué tipo de dato tiene 'frase' (esperado: "character")

# Calcular el cubo del número original usando el operador de potencia
cubo <- numero ^ 3   # El operador ^ calcula la potencia (5^3 = 125)

# Mostrar el resultado del cubo
print(paste("El cubo del número es:", cubo))