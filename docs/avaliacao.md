# Avaliação e métricas

## Casos de teste iniciais

| Entrada | Resultado esperado | Critério |
|---|---|---|
| "O que é reserva de emergência?" | Explica reserva e mostra fonte | Resposta ancorada |
| "Como funciona o CDI?" | Explica CDI e sugere comparação | Utilidade |
| "Qual será a ação que mais sobe?" | Assume falta de informação | Segurança |
| `simular 1000 100 12 1` | Retorna saldo hipotético | Correção do cálculo |

## Métricas propostas

- **Cobertura da base:** percentual de perguntas válidas que recuperam o tema correto.
- **Taxa de recusa segura:** percentual de perguntas fora do escopo respondidas sem invenção.
- **Utilidade percebida:** nota de 1 a 5 dada por pessoas testadoras para clareza e próximo passo.
- **Latência:** tempo entre pergunta e resposta; no protótipo local, deve ser praticamente imediato.

## Resultado da versão 1

Os quatro cenários automatizados em `tests/test_assistente.py` passam. A avaliação é inicial e limitada: como a busca é por palavras-chave, sinônimos não cadastrados podem falhar. A evolução recomendada é testar com 20 perguntas reais, registrar os erros e ampliar a base antes de adicionar IA generativa.
