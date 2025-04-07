"""
2)Desarrolla un programa que solicite al usuario
un número entero y determine la cantidad de 
dígitos que contiene.
"""

#pedimos al usuario un numero 
numero = int(input("ingrese un numero entero: "))

#inicializamos la variable digito en 0 para contar cuantos digitos 
#tiene el numero que ingreso el usuario
digito = 0

#creo un bucle while que mientras numero sea mayor a 0
#divida por 10 , por cada iteracion suma 1 a la variable digito
while numero > 0:
    numero = numero // 10
    digito += 1

#mostramos por pantalla cuantos digitos tiene el numero
#ingresado por el usuario
print(digito)
