"""
10) Escribe un programa que invierta el orden de los dígitos
de un número ingresado por el usuario. Ejemplo:
si el usuario ingresa 547, el programa debe mostrar 745.
"""

numero = int(input("Ingrese un número: "))
numero_invertido = 0

#Trabajamos con el valor absoluto del número
num_absoluto = abs(numero)

while num_absoluto > 0:
    #Extraer el último dígito
    digito = num_absoluto % 10

    #Añadir el dígito al número invertido
    numero_invertido = numero_invertido * 10 + digito
    
    #Eliminar el último dígito
    num_absoluto //= 10  

#Si el número original es negativo, ajustamos el signo
if numero < 0:
    numero_invertido *= -1

print(f"El número invertido es: {numero_invertido}")
