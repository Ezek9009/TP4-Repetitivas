"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio
entre 0 y 9. Al final, el programa debe mostrar cuántos
intentos fueron necesarios para acertar el número.
"""
#importamos la libreria random para el numero aleatorio
import random

#la variable salida es la que se encarga de salir del bucle while
salida = True

#el numero que el usuario tiene que adivinar
numero_aleatorio = random.randint(0, 9)

#la variable reservada para el usuario
numero_usuario = 0

#contador de intentos
contador_intentos = 0

#bucle mientras que salida sea verdadera:
while salida:
    #pedimos al usuario que ingrese un numero
    numero_usuario = int(input("adivina el numero entre 0 y 9: "))

    #si el numero que ingreso el usuario es igual al numero aleatorio
    if numero_usuario == numero_aleatorio:

        #la variable salida pasa a False
        salida = False

        #y la variable contador se suma 1 intento(si es que lo adivina de un
        #intento)
        contador_intentos += 1
    else:
        #en caso contrario , suma 1 al contador de intentos
        #e imprime que no es el numero correcto
        contador_intentos += 1
        print("numero incorrecto..")
        
#si adivina el numero muestra la cantidad de intentos.
print(f"felicidades! adivinaste.. \ncantidad de intentos: {contador_intentos}")
    