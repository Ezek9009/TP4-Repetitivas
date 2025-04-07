"""
9)Elabora un programa que permita al usuario ingresar
100 números enteros y luego calcule la media de esos valores.
(Nota: puedes probar el programa con una cantidad menor, 
pero debe poder procesar 100 números cambiando solo un valor).
"""

#cant_numeros es el maximo de numeros que el usuario puede ingresar
cant_numeros = 3

#num_usuario es el numero que ingresa el usuario por teclado
num_usuario = 0

#suma se utiliza para sumar todos los numeros que el usuario ingresa
suma = 0

#para despues dividir suma / cant_numeros para asi obtener la media
promedio = 0

#con este bucle for se itera desde i hasta 100 (cant_numeros)
for i in range(cant_numeros):
    num_usuario = int(input("ingrese un numero entero: "))
    suma += num_usuario

#para despues dividir suma / cant_numeros para asi obtener la media
promedio = suma / cant_numeros

#muestra en pantalla el promedio de los numeros ingresados
print(f"el promedio es: {promedio}")

