#Programa que pida 10 números e imprima el promedio de estos.
#Se utilizan los conceptos del programa anterior de contador y acumulador
suma = 0
for i in range(10):
    num = int(input(" ingresar numero "))
    suma = suma + num
print(" el promedio de los numeros es ",suma/10)


