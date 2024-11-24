#Crea una programa que pida un número y calcule su factorial (El factorial de 
        #un número es el producto de todos los enteros entre 1 y el propio número y se 
                #representa por el número seguido de un signo de exclamación. 
# Función para calcular el factorial y mostrar el proceso
def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        pasos = []  # Para almacenar los pasos del cálculo
        for i in range(1, n + 1):
            factorial *= i
            pasos.append(str(i))
        # Retorna el resultado y los pasos para mostrar en el formato requerido
        return factorial, "x".join(pasos)

# Pedir al usuario un número
numero = int(input("Introduce un número para calcular su factorial: "))

# Calcular el factorial y mostrar el resultado
resultado, pasos = calcular_factorial(numero)

# Mostrar el cálculo paso a paso
print(f"{numero}! = {pasos} = {resultado}")







