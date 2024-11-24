#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
#y la media de todos los números introducidos.
suma=0
contador=0
while True:
    num = int(input(" introducir num "))
    if num==0:
        print(" termino ciclo ")
        break
    else:
        suma=suma+num
        contador=contador+1

print(" la suma de los numeros es",suma)
print(" el promedio de los numeros es",suma/contador)