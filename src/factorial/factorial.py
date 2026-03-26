#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def procesar_entrada(entrada):
    if "-" in entrada:
        partes = entrada.split("-")

        # Caso: -hasta (ej: -10)
        if partes[0] == "":
            desde = 1
            hasta = int(partes[1])

        # Caso: desde- (ej: 5-)
        elif partes[1] == "":
            desde = int(partes[0])
            hasta = 60

        # Caso: desde-hasta (ej: 4-8)
        else:
            desde = int(partes[0])
            hasta = int(partes[1])

        for i in range(desde, hasta + 1):
            print(f"{i}! = {factorial(i)}")

    else:
        num = int(entrada)
        print(factorial(num))


# Entrada por argumento o input
if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    entrada = input("Ingrese número o rango (ej: 4-8, -10, 5-): ")

procesar_entrada(entrada)