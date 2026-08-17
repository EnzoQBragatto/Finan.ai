from pathlib import Path

from src.assistente import AssistenteFinanceiro
from src.simulador import simular_juros_compostos


RAIZ = Path(__file__).resolve().parents[1]


def executar_simulacao(comando: str) -> str:
    partes = comando.split()
    if len(partes) != 5:
        return "Formato: simular valor_inicial aporte_mensal meses taxa_mensal_percentual"
    try:
        saldo = simular_juros_compostos(float(partes[1]), float(partes[2]), int(partes[3]), float(partes[4]))
    except ValueError as erro:
        return f"Não foi possível simular: {erro}"
    return f"Cenário hipotético: ao fim de {partes[3]} meses, o saldo seria R$ {saldo}."


def main() -> None:
    assistente = AssistenteFinanceiro(RAIZ / "data" / "base_conhecimento.json")
    print("FinanIA: assistente financeiro educacional. Digite 'sair' para encerrar.")
    print("Para cálculos: simular valor_inicial aporte_mensal meses taxa_mensal_percentual")
    while True:
        mensagem = input("\nVocê: ").strip()
        if mensagem.lower() in {"sair", "exit", "quit"}:
            print("FinanIA: Até mais! Planejamento é construído aos poucos.")
            break
        if not mensagem:
            print("FinanIA: Escreva uma pergunta para eu poder ajudar.")
        elif mensagem.lower().startswith("simular"):
            print(f"FinanIA: {executar_simulacao(mensagem)}")
        else:
            print(f"FinanIA: {assistente.responder(mensagem)}")


if __name__ == "__main__":
    main()
