import unittest
from datetime import date, datetime, timedelta

from tarefa import Tarefa


class TestConcluir(unittest.TestCase):
    def test_concluir_tarefa_altera_concluido_para_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)

    def test_concluir_tarefa_concluida_mantem_concluida_como_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)


class TestAdiarNotificacao(unittest.TestCase):
    def test_adia_notificacao_em_10_minutos(self):
        dt_original = datetime(2022, 4, 14, 9, 10)
        adiar_em = 10

        tarefa = Tarefa("Estudar Python", data_notificacao=dt_original)
        tarefa.adiar_notificacao(adiar_em)

        dt_esperado = dt_original + timedelta(minutes=adiar_em)

        self.assertEqual(tarefa.data_notificacao, dt_esperado)


class TestAdicionaDescricao(unittest.TestCase):
    def test_adiciona_descricao_a_tarefa(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.adicionar_descricao("Aprender Python")

        self.assertEqual(tarefa.descricao, "Aprender Python")


class TestVerificaSeTarefaEstaAtrasada(unittest.TestCase):
    def test_verificar_se_tarefa_esta_atrasada_quando_data_for_maior_que_hoje(self):
        tarefa = Tarefa("Estudar Python", data=date(2022, 4, 15))

        self.assertEqual(tarefa.atrasada(), False)


unittest.main()
