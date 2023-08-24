import os

print("==========BIENVENIDO AL  SISTEMA============\n")

print("===LISTA CURSOS==\n")
n = int(input("Ingrese la cantidad de cursos que ingresará:  "))
listaCursos = []

for i in range(0, n): 
    cursos = str(input(f"Ingrese el curso {i + 1} :"))
    listaCursos.append(cursos)
print("Agregado exitosamente\n")

print("Los cursos agregados son: ")
for i in listaCursos:
    print(i)

print("===ALMACEN PERSONAS==\n")

n = int(input("Ingrese la cantidad de personas que ingresará:  "))
personas = {}

for i in range(0, n): 
    nombre = str(input(f"Ingrese el nombre de persona {i + 1} :"))
    personas[i] = nombre
print("Agregado exitosamente\n")

nperson = int(input("Ingrese su número de persona: "))
src = personas.get(nperson)

print(f"Su nombre es: {src}\n")

print("===TUPLAS==\n")

datos = ()

print("Ingrese los datos: ")
entero = int(input("Ingrese un número entero: "))
decimal = float(input("Ingrese un número decimal: "))
cadena = str(input("ingrese una cadena de texto: "))

for i in range(0, 2):
    coleccion = input(f"ingrese el valor {i} a la coleccion:  ")

print("los tipos de datos son: ")
print(type(entero))
print(type(decimal))
print(type(cadena))
print(type(coleccion))


print("===DICCIONARIO==\n")

diccionario = {"Euro" : "E", "Dollar" : "$", "Yen": "Y"}
valor = float(input("ingrese el valor a convertir: "))
conver = int(input("Convertir a: Marque 1 para Euro, 2 para Dollar y 3 para Yen"))

if conver == 1:
    total1 = valor * 4.096,17
    print(f"Equivale a {total1} dolares")


