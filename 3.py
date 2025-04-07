"""
3) Escribe un programa que sume todos los números enteros
 comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.
"""
#creamos 2 variables para ingresar los numeros
numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese otro numero: "))

#con esta variable tenemos el valor de la suma
suma = 0

#este bucle for, itera desde numero1+1 hasta numero2, sin incluir el valor
#de numero2
for i in range(numero1+1,numero2):
    suma += i

#mostramos en pantalla la suma
print(suma)