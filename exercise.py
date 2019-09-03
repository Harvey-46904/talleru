'''Escriba un algoritmo que solicite un número por pantalla, y visualice 
el  Factorial  de  dicho  valor  ingresado.  (Consulte  la  factorial  de  un 
número'''
import os
'''def factorial(a):
    if a == 1:
        return 1
    return a*factorial(a-1)

x=int(input("Digite numero deseado: "))
print(factorial(x))'''

'''PALABRAS'''
palabra=[]
continuar=False
def opcion():
 
    print ("BIENVENIDO")
    print ("[1] Ingrese Palabra")
    print ("[2] Mostrar Palabra")
    print ("[3] Mostrar Palabra Invertida")
    print ("[4] Salir")

def alimentar():
    N=int(input("Digite numero de letras: "))
    for i in range (1,N+1) :
        print ("Digite letra ",i," de la palabra")
        L=str(input("Digite letra: "))
        palabra.append (L)    

def men(a):
    if a==1:
        alimentar()    
    elif a==2:
        for letter in palabra:
            print (letter)
    elif a==3:
        palabrainvertida=palabra[::-1]
        for ti in palabrainvertida:
            print(ti)
    
def total():
    print (palabra)
    while continuar==False:
        opcion()
        des=int(input("Seleccion Opcion: "))
        if des == 4:
            break
        else:
            men(des)
#total()

'''Monedas '''

print ("")
moneda=int(input("Digite valor a retirar: "))
print ("")
def cambios(money):
    if money == 0 :
        print("")
    if money >= 1 and money <5:
        print ("Moneda: 1")
        cambios(money-1)
    if money >= 5 and money <10:
        print ("Moneda: 5")
        cambios(money-5)
    if money >= 10 and money <20:
        print ("Moneda: 10")
        cambios(money-10)
    if money >= 20 and money <50:
        print ("Moneda: 20")
        cambios(money-20)
    if money >= 50 and money <100:
        print ("Moneda: 50")
        cambios(money-50)
    if money >= 100:
        print ("Moneda: 100")
        cambios(money-100)
cambios(moneda)