import math
import sys


class RPNError(Exception):
    pass


def evaluar(expr):
    pila = []
    mem = {f"{i:02}": 0.0 for i in range(10)}

    def pop(n=1):
        if len(pila) < n:
            raise RPNError("Pila insuficiente")
        if n == 1:
            return pila.pop()
        return [pila.pop() for _ in range(n)]

    for token in expr.split():
        try:

            pila.append(float(token))
            continue
        except ValueError:
            pass

        # Constantes
        if token == "p":
            pila.append(math.pi)
        elif token == "e":
            pila.append(math.e)
        elif token == "j":
            pila.append((1 + math.sqrt(5)) / 2)

        elif token in "+-*/":
            b, a = pop(2)
            if token == "+":
                pila.append(a + b)
            elif token == "-":
                pila.append(a - b)
            elif token == "*":
                pila.append(a * b)
            elif token == "/":
                if b == 0:
                    raise RPNError("División por cero")
                pila.append(a / b)

        # Funciones
        elif token == "sqrt":
            pila.append(math.sqrt(pop()))
        elif token == "log":
            pila.append(math.log10(pop()))
        elif token == "ln":
            pila.append(math.log(pop()))
        elif token == "ex":
            pila.append(math.exp(pop()))
        elif token == "10x":
            pila.append(10 ** pop())
        elif token == "1/x":
            x = pop()
            if x == 0:
                raise RPNError("División por cero")
            pila.append(1 / x)
        elif token == "yx":
            b, a = pop(2)
            pila.append(a**b)

        #  (grados)
        elif token == "sin":
            pila.append(math.sin(math.radians(pop())))
        elif token == "cos":
            pila.append(math.cos(math.radians(pop())))
        elif token == "tg":
            pila.append(math.tan(math.radians(pop())))
        elif token == "asin":
            pila.append(math.degrees(math.asin(pop())))
        elif token == "acos":
            pila.append(math.degrees(math.acos(pop())))
        elif token == "atg":
            pila.append(math.degrees(math.atan(pop())))

        elif token == "chs":
            pila.append(-pop())

        #  pila
        elif token == "dup":
            if not pila:
                raise RPNError("Pila insuficiente")
            pila.append(pila[-1])
        elif token == "swap":
            b, a = pop(2)
            pila.extend([b, a])
        elif token == "drop":
            pop()
        elif token == "clear":
            pila.clear()

        # Mem
        elif token.startswith("STO"):
            idx = token[3:]
            if idx not in mem:
                raise RPNError("Memoria inválida")
            mem[idx] = pop()
        elif token.startswith("RCL"):
            idx = token[3:]
            if idx not in mem:
                raise RPNError("Memoria inválida")
            pila.append(mem[idx])

        else:
            raise RPNError(f"Token inválido: {token}")

    if len(pila) != 1:
        raise RPNError("La pila no terminó con un único valor")

    return pila[0]


def main():
    try:
        expr = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("RPN> ")
        resultado = evaluar(expr)
        print(resultado)
    except RPNError as e:
        print(f"Error: {e}")
    except Exception:
        print("Error inesperado")


if __name__ == "__main__":
    main()
