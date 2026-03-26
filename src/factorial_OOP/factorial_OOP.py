import sys

# Clase que encapsula la lógica del factorial
class Factorial:

    # Constructor (no necesita parámetros por ahora)
    def __init__(self):
        pass

    # Método para calcular factorial de un número
    def calcular(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.calcular(n - 1)

    # Método principal que ejecuta el cálculo en un rango
    def run(self, minimo, maximo):
        for i in range(minimo, maximo + 1):
            print(f"{i}! = {self.calcular(i)}")


# Función para procesar entrada (igual lógica que antes)
def procesar_entrada(entrada):
    if "-" in entrada:
        partes = entrada.split("-")

        if partes[0] == "":
            minimo = 1
            maximo = int(partes[1])
        elif partes[1] == "":
            minimo = int(partes[0])
            maximo = 60
        else:
            minimo = int(partes[0])
            maximo = int(partes[1])
    else:
        minimo = maximo = int(entrada)

    return minimo, maximo


# Entrada por argumento o input
if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    entrada = input("Ingrese número o rango (ej: 4-8, -10, 5-): ")

minimo, maximo = procesar_entrada(entrada)

# Crear objeto de la clase y ejecutar
f = Factorial()
f.run(minimo, maximo)