#Crea un programa que permita adivinar un número. La aplicación genera un 
#número aleatorio del 1 al 100
import random
numero=random.randint(1,100)#numero que se deve adivinar
intentos=1#variable del control
adivinado=False
print("bienbenido a la partida")
while intentos <= 10:
    print("intento numero: ",intentos)
    print("ingresa numero")
    num = int(input())#solicitar numero a comparar
    if(num==numero):
        print("adivinaste el numero")
        print("fin de la partida")
        adivinado=True
        break
    elif(numero >num ):
        print("el numero ingresado es mayor, intenta de nuevo")
        intentos+=1
    else:
         print("el numero ingresado es menor, intenta de nuevo")
         intentos+=1
if adivinado ==False:
    print("no le atinaste")