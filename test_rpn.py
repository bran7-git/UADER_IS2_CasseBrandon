import unittest
from rpn import evaluar, RPNError
import math

class TestRPN(unittest.TestCase):

    #  Casos correctos 
    def test_suma(self):
        self.assertEqual(evaluar("3 4 +"), 7)

    def test_expresion_compleja(self):
        self.assertEqual(evaluar("5 1 2 + 4 * + 3 -"), 14)

    def test_multiplicacion_suma(self):
        self.assertEqual(evaluar("2 3 4 * +"), 14)

    def test_float(self):
        self.assertAlmostEqual(evaluar("2.5 2 *"), 5.0)

    def test_negativos(self):
        self.assertEqual(evaluar("-3 -2 *"), 6)

    #  Const
    def test_pi(self):
        self.assertAlmostEqual(evaluar("p"), math.pi)

    def test_e(self):
        self.assertAlmostEqual(evaluar("e"), math.e)

    # Func
    def test_sqrt(self):
        self.assertEqual(evaluar("9 sqrt"), 3)

    def test_log(self):
        self.assertEqual(evaluar("100 log"), 2)

    def test_potencia(self):
        self.assertEqual(evaluar("2 3 yx"), 8)

    def test_inverso(self):
        self.assertEqual(evaluar("2 1/x"), 0.5)

    # Trigon
    def test_sin(self):
        self.assertAlmostEqual(evaluar("90 sin"), 1)

    def test_cos(self):
        self.assertAlmostEqual(evaluar("0 cos"), 1)

    #  Pila 
    def test_dup(self):
        self.assertEqual(evaluar("3 dup *"), 9)

    def test_swap(self):
        self.assertEqual(evaluar("3 4 swap -"), 1)

    def test_drop(self):
        self.assertEqual(evaluar("3 4 drop"), 3)

    # Mem
    def test_memoria(self):
        self.assertEqual(evaluar("5 STO00 RCL00"), 5)

    #  ERRORES 
    def test_division_por_cero(self):
        with self.assertRaises(RPNError):
            evaluar("3 0 /")

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            evaluar("3 4 &")

    def test_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            evaluar("+")

    def test_pila_final_invalida(self):
        with self.assertRaises(RPNError):
            evaluar("3 4")

    def test_memoria_invalida(self):
        with self.assertRaises(RPNError):
            evaluar("5 STO99")

    #Más func
    def test_ln(self):
        self.assertAlmostEqual(evaluar("2.718281828 ln"), 1, places=2)

    def test_ex(self):
        self.assertAlmostEqual(evaluar("1 ex"), math.e)

    def test_10x(self):
        self.assertEqual(evaluar("2 10x"), 100)

    def test_chs(self):
        self.assertEqual(evaluar("5 chs"), -5)

    #  Trig invers
    def test_asin(self):
        self.assertAlmostEqual(evaluar("1 asin"), 90)

    def test_acos(self):
        self.assertAlmostEqual(evaluar("1 acos"), 0)

    def test_atg(self):
        self.assertAlmostEqual(evaluar("1 atg"), 45)

    #  Clear 
    def test_clear(self):
        with self.assertRaises(RPNError):
            evaluar("3 4 clear")

    # Divis con error 
    def test_inv_error(self):
        with self.assertRaises(RPNError):
            evaluar("0 1/x")

    #  Stack vacío dup 
    def test_dup_error(self):
        with self.assertRaises(RPNError):
            evaluar("dup")

if __name__ == "__main__":
    unittest.main()