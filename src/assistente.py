import json
import re
from pathlib import Path
from typing import Any


class AssistenteFinanceiro:
    def __init__(self, caminho_base: str | Path):
        with open(caminho_base, encoding="utf-8") as arquivo:
            self.base: list[dict[str, Any]] = json.load(arquivo)
        self.ultimo_tema: str | None = None

    @staticmethod
    def _tokens(texto: str) -> set[str]:
        return set(re.findall(r"[\wÀ-ÿ]+", texto.lower()))

    def responder(self, pergunta: str) -> str:
        tokens = self._tokens(pergunta)
        melhor_item = None
        maior_pontuacao = 0
        for item in self.base:
            pontuacao = len(tokens.intersection(self._tokens(" ".join(item["palavras_chave"]))))
            if pontuacao > maior_pontuacao:
                maior_pontuacao, melhor_item = pontuacao, item

        if not melhor_item:
            contexto = f" O último tema da conversa foi {self.ultimo_tema}." if self.ultimo_tema else ""
            return (
                "Ainda não tenho informação suficiente para responder com segurança."
                f"{contexto} Você pode reformular a dúvida ou perguntar sobre reserva, orçamento, juros, CDI ou dívidas?"
            )

        self.ultimo_tema = melhor_item["titulo"]
        return (
            f"{melhor_item['resposta']}\n\n"
            f"Próximo passo: {melhor_item['proximo_passo']}\n"
            f"Fonte: {melhor_item['fonte']}\n\n"
            "Este conteúdo é educativo e não é recomendação financeira personalizada."
        )
