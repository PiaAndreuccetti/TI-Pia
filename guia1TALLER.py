
# EJ 1
from math import sqrt


def ej_1():
    name= "Pia"
    print("el nombre es"+ " " + name)

#EJ 2
def sum(x, y):
    return x + y

result_of_sum = sum(3, 5)
print(result_of_sum)

# EF 3
def minus(x,y):
     return x - y
print(minus(10, 5))

# EJ 4
def divide(x, y):
    return x / y
print(divide(4,2))

#EJ 5
def multiply(a, y):
    return a * y
print(multiply(3,2))

#EJ 6
def sqrt_custom(x):
    return sqrt(x)
print(sqrt_custom(9))

#EJ 7
def power(x, y):
    return x ** y
print(power(2, 3))

#EJ 8
def par(x):
    if x % 2 ==0:
        print("true")
    else:
        print("false")

par(5)

#EJ 9
newlist=["Martin","Pedro","Juan","Agustín"]
def change_name(i, new_name):
    newlist[i]=new_name
print(newlist)
change_name(2,"pia")
print(newlist)

#EJ 10
listnumers=[1,2,3,4,5,6,7,8,9,10]
total=0
for numbers in listnumers:
    total=total+numbers

#EJ 11
def nombrecompleto(nombre, apellido):
    print(nombre + " "+ apellido)
    nombre=nombre.lower()
    apellido=apellido.lower()
    print(nombre +" "+ apellido)
    nombre=nombre.title()
    apellido=apellido.title()
    print(nombre +" "+ apellido)
    nombre=nombre.upper()
    apellido=apellido.upper()
    print(nombre +" "+ apellido)

print(nombrecompleto("Pia","Andreuccetti"))

#EJ 12
def ordenalfa(a,b):
    newlist=[a,b]
    newlist.sort()
    print(newlist)

ordenalfa("pia","capa")

#EJ 13
def change(valor_pagado,valor_a_pagar):
    return valor_pagado-valor_a_pagar
change(20,10)
print(change(20,10))

#EJ 14
newlist=["Pia","Santi","Kevin"]
def registro(name):
    if name in newlist:
        print("RESIGTRADO")
    else:
        print("NO REGISTRADO")

registro("Pia")
registro("Pablo")

#EJ 15
nombre="Agustín"
nombre[0]
nombre[-1]
print(nombre[0])
print(nombre[-1])

#EJ 16
def costoentrada(edad):
    if edad<= 4:
        return 0 
    elif edad >4 and edad <17:
        return 50
    elif edad >17 and edad <50:
        return 30
    else:
        return 10

edadadolescente=14
edadabuelo=66
print(costoentrada(edadadolescente)+costoentrada(edadabuelo))

# EJ 17
semana=["Lunes","Martes","Miercoles","Jueves","Viernes"]
finde=["Sabado","Domingo"]
def quediaes(dia):
    if dia in semana:
        print("Día laboral")
    elif dia in finde:
        print("Día no laboral")
    else:
        print("Día no válido")
    
quediaes(input(" ¿Que día es?"))

#EJ 18
#EJ 19
def daystohours(dias):
    if dias>=0:
        print(dias*24)
    else:
        print("numero positivo")
daystohours(int(input("Cantidad de dias")))

#EJ 20
def perímetro(altura,largo):
    return altura + altura + largo + largo
print(perímetro(20,30))

#EJ 21

#EJ 22
mesesdelaño=["enero", "febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre",]
def numdemes(mes):
    if mes> 0 and mes<13:
        mesesdelaño[mes-1]
        print(mesesdelaño[mes-1])
numdemes(int(input("Dame un numero")))

#EJ 23

