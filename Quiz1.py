import os

print("==========BIENVENIDO AL  SISTEMA============\n")

print("===1. LISTA CURSOS==\n")
n = int(input("Ingrese la cantidad de cursos que ingresará:  "))
listaCursos = []

for i in range(0, n): 
    cursos = str(input(f"Ingrese el curso {i + 1} :"))
    listaCursos.append(cursos)
print("Agregado exitosamente\n")

print("Los cursos agregados son: ")
for i in listaCursos:
    print(i)

print("===2. ALMACEN PERSONAS==\n")

n = int(input("Ingrese la cantidad de personas que ingresará:  "))
personas = {}

for i in range(0, n): 
    nombre = str(input(f"Ingrese el nombre de persona {i + 1} :"))
    personas[i] = nombre
print("Agregado exitosamente\n")

nperson = int(input("Ingrese su número de persona: "))
src = personas.get(nperson)

print(f"Su nombre es: {src}\n")

print("===4. TUPLAS==\n")

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


print("===3. DICCIONARIO==\n")

diccionario = {"Euro" : 4473.59, "Dolar" : 4110.43, "Yen": 28.18}
conver = int(input("¿A qué moneda desea Convertir? Digite el número equivalente\n 1.Euro\n 2.Dolar \n 3.Yen \n >>>:  "))
valor = float(input("ingrese el valor en pesos a convertir: "))


if conver == 1:
    total1 = valor / diccionario.get("Euro")
    print(f"Equivale a {total1} Euros")
elif conver == 2:
    total2 = valor / diccionario.get("Dolar")
    print(f"Equivale a {total2} Dólares")
elif conver == 3:
    total3 = valor / diccionario.get("Yen")
    print(f"Equivale a {total3} Yenes")
else:
    print("La moneda que ingresó no se encuentra en el diccionario")



