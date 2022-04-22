import unittest

from calculadora_de_notas import Turma


class TestGetMedia(unittest.TestCase):
    def test_get_media_deve_retornar_a_media_da_turma(self):
        turma = [
            ["João", 5],
            ["Maria", 7],
            ["José", 8],
            ["Pedro", 5],
            ["Paulo", 3],
            ["Ana", 8],
            ["Júlia", 10],
        ]

        calcula = Turma()

        self.assertEqual(calcula.get_media(turma), 6)


class TestGetMaiorNota(unittest.TestCase):
    def test_get_maior_nota_deve_retornar_a_maior_nota_da_turma(self):
        turma = [
            ["João", 5],
            ["Maria", 7],
            ["José", 8],
            ["Pedro", 5],
            ["Paulo", 3],
            ["Ana", 8],
            ["Júlia", 4],
        ]

        calcula = Turma()

        self.assertEqual(calcula.get_maior_nota(turma), 8)


class TestGetMenorNota(unittest.TestCase):
    def test_get_menor_nota_deve_retornar_a_menor_nota_da_turma(self):
        turma = [
            ["João", 5],
            ["Maria", 7],
            ["José", 8],
            ["Pedro", 5],
            ["Paulo", 3],
            ["Ana", 8],
            ["Júlia", 4],
        ]

        calcula = Turma()

        self.assertEqual(calcula.get_menor_nota(turma), 3)


class TestGetAprovados(unittest.TestCase):
    def test_get_aprovados_deve_retornar_aprovados_da_turma(self):
        turma = [
            ["João", 5],
            ["Maria", 7],
            ["José", 8],
            ["Pedro", 5],
            ["Paulo", 3],
            ["Ana", 8],
            ["Júlia", 4],
        ]

        calcula = Turma()

        self.assertEqual(
            calcula.get_aprovados(turma, 6),
            ["Maria", "José", "Ana"],
        )


class TestGetReprovados(unittest.TestCase):
    def test_get_reprovados_deve_retornar_reprovados_da_turma(self):
        turma = [
            ["João", 5],
            ["Maria", 7],
            ["José", 8],
            ["Pedro", 5],
            ["Paulo", 3],
            ["Ana", 8],
            ["Júlia", 4],
        ]

        calcula = Turma()

        self.assertEqual(
            calcula.get_reprovados(turma, 6),
            ["João", "Pedro", "Paulo", "Júlia"],
        )


class TestGetNota(unittest.TestCase):
    def test_get_nota_deve_retornar_nota_em_letra(self):
        calcula = Turma()

        self.assertEqual(calcula.get_nota(9), "A")
        self.assertEqual(calcula.get_nota(8), "B")
        self.assertEqual(calcula.get_nota(6), "C")
        self.assertEqual(calcula.get_nota(4), "D")
        self.assertEqual(calcula.get_nota(2), "E")
        self.assertEqual(calcula.get_nota(0), "F")
        self.assertEqual(calcula.get_nota(10), "A+")


unittest.main()
