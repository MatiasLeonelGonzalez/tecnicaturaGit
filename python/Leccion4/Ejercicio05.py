# Clase 5 video 2
# Ejercicio 5: Factorial de un numero positivo
# Hacer un programa para calcular el factorial de un numero positivo

numero = int(input("digite un numero: "))
while numero < 0:  # mientras el numero sea negativo
    print("Error -> El numero tiene que ser positivo")
    numero = int(input("digite un numero: "))
factorial = 1  # la variable para calcular el factorial
for i in range(1, numero + 1):
    factorial *= i
print(f"\nEl factorial del numero {numero} positivo ingresado es: {factorial}")

# clase 5 video 3
