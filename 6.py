"""
6) Desarrolla un programa que imprima en pantalla
todos los números pares comprendidos 
entre 0 y 100, en orden decreciente.
"""

#este bucle for, va desde 100 hasta 0 con paso 1
#pero solo si es par, se imprime en pantalla
for i in range(100,0,-1):
    if i % 2 == 0:
        print(i)