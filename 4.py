"""
4) Elabora un programa que permita al usuario ingresar números enteros
 y los sume en secuencia. El programa debe detenerse y mostrar
el total acumulado cuando el usuario ingrese un 0. 
"""
#numero es la variable con la cual el usuario ingresa valores enteros
numero = 0

#suma es la variable que suma los numeros enteros (positivos o negativos)
suma = 0

#salida es la variable para terminar el bucle while
salida = True

#mientras que salida sea verdadera(True)
while salida:
    #el usuario ingresa un numero
    numero = int(input("ingrese un numero (0 para finalizar): "))

    #si el numero ingresado es 0 se termina el bucle
    if numero == 0:
        salida = False

    #en caso contrario sumamos el numero a la variable suma    
    else:
        suma += numero

#mostramos en pantalla la suma de los numeros
print(f"la suma de los numeros ingresados es: {suma}")

