# CLASE 1 video 1

# Colecciones en Python

# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores

# lista = ariel, liliana, natalia, osvaldo

nombres = ["naty", "osvaldo", "lili", "ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])  # (para ver el ulitmo de la lista)

# video 2

print(nombres)
print(nombres[0:2])  # solo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[1:])

# Modificamos un valor

nombres[2] = "liliana"
nombres[0] = "natalia"
print(nombres)

# Iterar una lista

for nombre in nombres:  # nombre es singular, la lista es plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

# video 3

# Preguntamos cuantos elementos tiene

print(len(nombres))  # le pasamos como parametro la lista

# agregamos un elemento

nombres.append("marcelo")
print(nombres)

# Insertar un elemento en un indice especifico

nombres.insert(1, "alberto")
print(nombres)
nombres.insert(3, "debora")
print(nombres)

# Eliminamos un elemento

nombres.remove("alberto")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico

del nombres[2]  # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos

nombres.clear()
print(nombres)

# Eliminar la lista

del nombres
# print(nombres)  # nos salta un error por que ya borro la lista!

# video 4 en EjercicioRango.py

# video 6

# Definimos una tupla
cocina = "cuchara", "cuchillo", "tenedor"
print(cocina)
print(len(cocina))

# Acceder a un elemento,para esto utilizamos corchetes no parentesis

print(cocina[0])

# Mostrar de manera inversa

print(cocina[-1])

# Acceder a un rango

print(cocina[0:1])

# EJEMPLO

verduras = ("papa",)  # una tupla necesita aunque sea de un elemento la coma (,)
# de lo contrario solo seria un tipo string cadena

# video 7

for cocinar in cocina:  # print esta usando \n para saltos de linea
    print(cocinar, end=" ")  # Usamos end= para eliminar saltos de linea

"""cocina[0] = "plato"  # da error
print(cocina)

cocinalista = list(cocina)
cocinalista[0] = "plato"
cocina = tuple(cocinalista)
print("\n", cocina)

del cocina  # esto es para eliminar
print(cocina)
"""
# CLASE 2
# #video 1 y 2
# Tipo set (orden alertorio)(y no se repiten elementos)
planetas = {"marte", "jupiter", "venus"}  # ejemplo
print(len(planetas))  # usamos la funcion len= length significa largo

# revisar si un elemento eciste dentro de set
print("marte" in planetas)  # respetar mayusculas,minusculas y acentos

# agregar un elemento
planetas.add("tierra")  # add es una funcion
print(planetas)

# Eliminar elementos, puede generar un error si el elemento no existe

planetas.remove("jupiter")  # esta funcion ante un mal ingreso del elemanto da error
print(planetas)

planetas.discard("tierra")  # esta funcion no nos presenta ningun error

# limpiar set

planetas.clear()
print(planetas)

# Eliminar set o conjunto

# del planetas # da error por que borra el set

# video 3

# 'maradona' :10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    "IDE": "Integrated development environment",
    "POO": "Programacion orientada a objetos",
    "SABD": "Sisitema de Administracion de base de datos",
}
print(len(diccionario))  # len se usa para verificar la cantidad de elementos
print(diccionario)

# acceder a un diccionario con la llave (key)

print(diccionario["IDE"])

# otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

# modificamos elementos
diccionario["IDE"] = "Entorno de desarrollo integrado"
print(diccionario)

# video 4
# como recorrer los elementos
for termino in diccionario:
    print(termino)

for termino in diccionario:  # recorremos mostrando solo las llaves
    print(termino)
for termino, valor in diccionario.items():
    print(termino, valor)

# otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)  # muestra solo las llaves

for valor in diccionario.values():  # usamos una funcion para acceder al valor
    print(valor)

# comprobar la ecistencia de algun elemento
print("IDE" in diccionario)  # devuelve un booleano

# agregar un elemento
diccionario["PK"] = "Primary key"
print(diccionario)

# eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# vaciar un diccionario
diccionario.clear()
print(diccionario)

# eliminar diccionario
del diccionario  # el diccionario se borra
# print(diccionario)  # da error por que se borro en la linea anterior

# video 5 explica que a las listas se les puede agregar cualquier tipo de dato.

# video 6

# concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9, 1])  # funcion para aggregar varios elementos a una lista
print(lista3)

print(lista3.index(5))  # funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) #esto daria un error por no ser el elemento parte de la lista

# como saber cuantos valores repetidos hay dentro de una lista

print(lista3.count(1))  # cuenta cuantos avlores iguales hay dentro de la lista

# para poner una lista al reves

lista3.reverse()
print(lista3)

# video 7

# para que una lista se multiplique repitiendo sus elementos

lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento

lista3.sort()  # ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True)  # ordena los elementos descendentemente
print(lista3)

# video 8

# repaso de tuplas

tupla = (
    3,
    "hola",
    6.78,
    [1, 2, 78],
    4,
    "hola",
)  # puede tener diferentes tipos de datos dentro
print(tupla)
print(4 in tupla)  # accuin booleana, su respuesta es de tipo booleana
# lo que podemos usar dentro de tuplas son: index, count, len
# en tuplas se puede convertir de tupla a lista y de lista a tupla
