# Clase 5 video 1:
# Ejercicio 4: Sumar numero pares denmtro de un rango
# Hacer un programa para suymar numeros pares dentro de un rango,por ejemplo:
# suma de numeros pares del 2 al 30
# suma= 240

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde va a llegar la suma: "))
suma = 0
for i in range(a, b + 1):
    if i % 2 == 0:  # esto es si elk numero es par
        suma += i
print(f"\nLa suma de numeros pares dentro del rango es: {suma}")
