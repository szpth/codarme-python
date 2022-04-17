import unittest
from datetime import date, timedelta

from lista_de_tarefas import ListaDeTarefas
from tarefa import Tarefa


class TestAdicionarTarefa(unittest.TestCase):
    def test_adiciona_tarefa_a_lista_de_tarefas(self):
        tarefa = Tarefa(titulo="Tarefa Teste")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa)

        # self.assertEqual(lista.get_tarefas()[0], tarefa)
        self.assertIn(tarefa, lista.get_tarefas())


class TestGetTarefas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_adicionadas(self):
        tarefa_um = Tarefa(titulo="Tarefa Teste 1")
        tarefa_dois = Tarefa(titulo="Tarefa Teste 2")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(
            lista.get_tarefas(),
            [
                tarefa_um,
                tarefa_dois,
            ],
        )


class TestGetTarefasAtrasadas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_atrasadas(self):
        tarefa_um = Tarefa(
            titulo="Tarefa Teste 1", data=(date.today() - timedelta(days=1))
        )
        tarefa_dois = Tarefa(
            titulo="Tarefa Teste 2", data=(date.today() - timedelta(days=1))
        )
        tarefa_dois.concluida = True

        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(
            lista.get_tarefas_atrasadas(),
            [
                tarefa_um,
            ],
        )

        self.assertNotEqual(
            lista.get_tarefas_atrasadas(),
            [
                tarefa_dois,
            ],
        )


class TestGetTarefasParaHoje(unittest.TestCase):
    def test_retorna_lista_de_tarefas_para_hoje(self):
        tarefa_um = Tarefa(titulo="Tarefa Teste 1", data=date(2022, 4, 13))
        tarefa_dois = Tarefa(titulo="Tarefa Teste 2", data=date(2022, 4, 14))

        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(
            lista.get_tarefas_para_hoje(),
            [
                tarefa_dois,
            ],
        )


unittest.main()
