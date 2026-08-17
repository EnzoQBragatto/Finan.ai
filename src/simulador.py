from decimal import Decimal, ROUND_HALF_UP


def simular_juros_compostos(valor_inicial: float, aporte_mensal: float, meses: int, taxa_mensal_percentual: float) -> Decimal:
    """Calcula um cenário hipotético com aportes no fim de cada mês."""
    if valor_inicial < 0 or aporte_mensal < 0 or meses <= 0 or taxa_mensal_percentual < 0:
        raise ValueError("Use valores não negativos e uma quantidade de meses maior que zero.")

    saldo = Decimal(str(valor_inicial))
    aporte = Decimal(str(aporte_mensal))
    taxa = Decimal(str(taxa_mensal_percentual)) / Decimal("100")
    for _ in range(meses):
        saldo = saldo * (Decimal("1") + taxa) + aporte
    return saldo.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
