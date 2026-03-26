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
        desde, hasta = map(int, entrada.split("-"))
        for i in range(desde, hasta + 1):
            print(f"{i}! = {factorial(i)}")
    else:
        num = int(entrada)
        print(factorial(num))

# Entrada por argumento o por input
if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    entrada = input("Ingrese un número o rango (ej: 4-8): ")

procesar_entrada(entrada)