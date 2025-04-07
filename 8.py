"""
8)Escribe un programa que permita al usuario ingresar 100 números enteros.
Luego, el programa debe indicar cuántos de estos números son pares,
cuántos son impares, cuántos son negativos y cuántos son positivos.
(Nota: para probar el programa puedes usar una cantidad menor,
pero debe estar preparado para procesar 100 números con un solo cambio).
"""
#cantidad de numeros que el usuario puede ingresar
cantidad_numeros = 100

#los numeros que ingresa el usuario
num_usuario = 0

#variables para contar : pares, impares, negativos, positivos
num_pares = 0
num_impares = 0
num_negativos = 0
num_positivos = 0

#este bucle for itera la cantidad de veces que cantidad_numeros
for i in range(cantidad_numeros):

    #solicitamos al usuario el numero que quiera ingresar
    num_usuario = int(input("ingrese un numero: "))

    #si el numero ingresado es par o impar
    if num_usuario % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
    
    #si el numero ingresado es positivo o negativo
    if num_usuario > 0:
        num_positivos += 1
    else:
        num_negativos += 1

#mostramos en pantalla los numeros: pares, impares, positivos, y negativos
print(f"numeros pares: {num_pares}")
print(f"numeros impares: {num_impares}")
print(f"numeros positivos: {num_positivos}")
print(f"numeros negativos: {num_negativos}")