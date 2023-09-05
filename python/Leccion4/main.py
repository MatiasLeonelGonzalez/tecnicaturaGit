# video 1

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
print(nombres)  # nos salta un error por que ya borro la lista!

# video 4 en EjercicioRango.py

# video 5
