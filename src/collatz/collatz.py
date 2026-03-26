import matplotlib.pyplot as plt

# Función que calcula los pasos de Collatz hasta llegar a 1
def collatz_steps(n):
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos

# Listas para graficar
numeros = []
iteraciones = []

# Calcular para números del 1 al 10000
for i in range(1, 10001):
    numeros.append(i)
    iteraciones.append(collatz_steps(i))

# Gráfico
plt.figure()
plt.scatter(numeros, iteraciones)
plt.xlabel("Número inicial (n)")
plt.ylabel("Cantidad de iteraciones")
plt.title("Conjetura de Collatz (1 a 10000)")
plt.show()