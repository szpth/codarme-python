import unittest

from calculadora import dividir, multiplicar, somar, subtrair


class TestSomar(unittest.TestCase):
    def test_soma_de_dois_numeros_inteiros(self):
        soma = somar(2, 4)
        self.assertEqual(soma, 6)

    def test_soma_de_numero_com_zero(self):
        self.assertEqual(somar(2, 0), 2)


class TestDividir(unittest.TestCase):
    def test_divide_numero_por_1_retorna_o_numero(self):
        self.assertEqual(dividir(10, 1), 10)

    def test_divide_por_zero_(self):
        self.assertEqual(dividir(10, 0), "Não é um número")


class TestMultiplicar(unittest.TestCase):
    def test_multiplicar_numero_por_ele_mesmo(self):
        self.assertEqual(multiplicar(10, 10), 100)

    def test_multiplica_numero_negativo(self):
        self.assertEqual(multiplicar(-5, 5), -25)


class TestSubtrair(unittest.TestCase):
    def test_subtrair_numero_e_da_negativo(self):
        self.assertEqual(subtrair(10, 15), -5)

    def test_subtrair_numero_com_zero_e_da_zero(self):
        self.assertEqual(subtrair(10, 0), 10)


unittest.main()
