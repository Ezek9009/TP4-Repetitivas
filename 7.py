"""
7) Crea un programa que calcule la suma de todos los números
 comprendidos entre 0 y un número entero positivo indicado por el usuario.
"""

suma = 0
#solicitamos al usuario que ingrese un numero entero positivo
numero = int(input("ingrese un numero entero positivo: "))

#si el numero es mayor a 0
if numero > 0:
    #se crea un bucle for que vaya desde 0 hasta el numero ingresado
    #sumando de a 1 hasta llegar al valor que el usuario ingresó
    #en la variable suma
    for i in range(0, numero+1):
        suma += i
#en caso contrario, mostramos en pantalla un mensaje que es un numero incorrecto
else:     
     print("debe ingresar un numero entero positivo..")
#mostramos en pantalla la suma de los numeros
print(f"la suma de todos los numeros comprendidos entre 0 y {numero} es {suma} ")