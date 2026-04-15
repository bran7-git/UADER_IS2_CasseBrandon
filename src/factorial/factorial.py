#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys  # Permite acceder a los argumentos de la línea de comandos

# Función que calcula el factorial de un número de forma recursiva
def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    else:
        # Llamada recursiva
        return n * factorial(n - 1)

# Función que procesa la entrada (número o rango)
def procesar_entrada(entrada):
    # Verifica si hay un guion (indica rango)
    if "-" in entrada:
        partes = entrada.split("-")  # Separa los valores

        # Caso: "-hasta" (ej: -10 → desde 1 hasta 10)
        if partes[0] == "":
            desde = 1
            hasta = int(partes[1])  # Convierte a entero

        # Caso: "desde-" (ej: 5- → desde 5 hasta 60)
        elif partes[1] == "":
            desde = int(partes[0])  # Convierte a entero
            hasta = 60

        # Caso: "desde-hasta" (ej: 4-8)
        else:
            desde = int(partes[0])
            hasta = int(partes[1])

        # Recorre el rango y calcula cada factorial
        for i in range(desde, hasta + 1):
            print(f"{i}! = {factorial(i)}")

    else:
        # Caso de un solo número
        num = int(entrada)  # Convierte a entero
        print(factorial(num))

# Verifica si se pasó un argumento por consola
if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    # Si no hay argumento, solicita al usuario que ingrese un valor
    entrada = input("Ingrese número o rango (ej: 4-8, -10, 5-): ")

# Procesa la entrada ingresada
procesar_entrada(entrada)