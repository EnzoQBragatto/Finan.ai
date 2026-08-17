import unittest
from pathlib import Path

from src.assistente import AssistenteFinanceiro
from src.app import executar_simulacao
from src.simulador import simular_juros_compostos


RAIZ = Path(__file__).resolve().parents[1]


class TestAssistenteFinanceiro(unittest.TestCase):
    def setUp(self):
        self.assistente = AssistenteFinanceiro(RAIZ / "data" / "base_conhecimento.json")

    def test_responde_assunto_conhecido_com_fonte(self):
        resposta = self.assistente.responder("Como criar uma reserva de emergência?")
        self.assertIn("reserva de emergência", resposta.lower())
        self.assertIn("Fonte:", resposta)

    def test_recusa_pergunta_fora_da_base(self):
        resposta = self.assistente.responder("Qual a previsão do tempo amanhã?")
        self.assertIn("não tenho informação suficiente", resposta.lower())

    def test_simulacao_com_aportes(self):
        self.assertEqual(str(simular_juros_compostos(1000, 100, 12, 1)), "2395.08")

    def test_formato_de_simulacao_invalido(self):
        self.assertIn("Formato:", executar_simulacao("simular 100"))


if __name__ == "__main__":
    unittest.main()
