import math  # Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)

# Dada la sigiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # definimos la tupla
# crear una lista que solo inclua numeros menores a 5 e imprima por consola [1, 3 , 2]

lista = []  # definimos la lista
# filtramos los elemenots menores a 6 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Clase 4 video 4
# Ejercicio de matematias
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo: "))
while numero < 0:
    print("Error -> Deberia ser un numero positivo: ")
    numero = int(input("Digite un numero positivo: "))
print(f"\nSu raiz cuadrada es: {math.sqrt(numero):.2f}")
