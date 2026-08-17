# FinanIA — Assistente Financeiro Educacional

Projeto desenvolvido para o Lab **"Construa Seu Assistente Virtual Com Inteligência Artificial"** do Bootcamp Santander/DIO.

O FinanIA ajuda pessoas que estão começando a organizar a vida financeira a entender conceitos básicos, como reserva de emergência, orçamento, juros e investimentos de renda fixa. Ele consulta uma base de conhecimento local, identifica a intenção da pergunta e oferece simulações educativas simples.

> Aviso: as respostas são educativas e não constituem recomendação de investimento, crédito ou aconselhamento financeiro individual.

## Funcionalidades

- Perguntas frequentes com busca por palavras-chave na base de conhecimento;
- Respostas claras, com fonte e próximo passo;
- Simulação de juros compostos (`simular`);
- Persistência do último tema conversado durante a sessão;
- Resposta segura quando não há informação suficiente;
- Testes automatizados e métricas de avaliação documentadas.

## Estrutura

```text
finania/
├── data/base_conhecimento.json
├── docs/{agente,prompts,avaliacao,pitch}.md
├── src/{assistente,simulador,app}.py
└── tests/test_assistente.py
```

## Como executar

Pré-requisito: Python 3.10 ou superior. Não há bibliotecas externas.

```powershell
cd "C:\Users\Enzo Bragatto\Desktop\Bootcamp Bradesco"
python -m src.app
```

Exemplos de mensagens:

```text
O que é reserva de emergência?
Como funciona o CDI?
simular 1000 100 12 1
```

O formato da simulação é: `simular valor_inicial aporte_mensal meses taxa_mensal_percentual`.

## Como testar

```powershell
python -m unittest discover -s tests -v
```

## Os 6 passos do desafio

1. [Documentação do agente](docs/agente.md)
2. [Base de conhecimento](data/base_conhecimento.json)
3. [Prompts e regras](docs/prompts.md)
4. [Aplicação funcional](src/app.py)
5. [Avaliação e métricas](docs/avaliacao.md)
6. [Pitch final](docs/pitch.md)

## Próximas evoluções

- Interface web com Streamlit;
- Inclusão de fonte oficial e data de atualização em cada conteúdo;
- Integração opcional com um modelo generativo, mantendo a recuperação e as regras de segurança;
- Histórico persistente, com consentimento explícito da pessoa usuária.
