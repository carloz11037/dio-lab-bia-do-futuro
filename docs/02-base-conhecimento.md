# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações e explicações |
| `produtos_financeiros.json` | JSON | Conhecer os produtos para que eles possam ser explicados ao cliente |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente para insights de forma didática  |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

- Foi expandido a base de dados de "protudos_financeiros" a fim de expandir os conhecimentos do agente
- Foi alterado o perfil do investidor padrão para um que se encaixasse mais com o contexto do agente. 

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

``` python
import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
produtos = json.load(f)
````

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados não são enviados completos no system prompt. Apenas as regras gerais do agente ficam fixas.
As informações da base de produtos financeiros são consultadas dinamicamente conforme a pergunta do usuário, e apenas os dados relevantes são inseridos no contexto da LLM no momento da resposta.
Esse processo reduz alucinações, melhora a precisão das respostas e torna o agente mais eficiente no uso de contexto.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.
O exemplo do contexto montado abaixo se baseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações relevantes,otimizando assim o consumo de tokens. Entretanto, vale lembrar que mais importante do que econimizar tokens, é ter as informações relevantes disponíveis.

```
Dados do Cliente:
- Nome: Maria Oliveira
- Idade: 26
- Profissão: Designer Gráfica
- Perfil investidor: Iniciante
- Conhecimento financeiro: Básico
- Renda mensal: R$ 3.800
- Patrimônio total: R$ 8.000
- Reserva de emergência atual: R$ 3.000
- Aceita risco: Não
- Objetivo principal: Aprender sobre investimentos e organizar a vida financeira

Metas:
- Construir reserva de emergência (R$ 12.000 até 2027-06)
- Aprender conceitos básicos de investimentos (até 2026-12)

Contexto da pergunta:
"Quais investimentos são mais seguros para começar?"

Produtos financeiros relevantes:
- Tesouro Selic (baixo risco, indicado para reserva de emergência)
- CDB Liquidez Diária (baixo risco, rendimento atrelado ao CDI)
- LCI/LCA (baixo risco, isento de IR, prazo mínimo de carência)

Instruções do agente:
- Explicar de forma simples e educativa
- Não fazer recomendações definitivas de compra
- Usar linguagem informal e acessível
- Priorizar educação financeira antes de decisões de investimento
- Sempre reforçar que investimentos envolvem riscos
...
