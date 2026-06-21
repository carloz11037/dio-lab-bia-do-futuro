#===============CARREGANDO DADOS==============

import pandas as pd
import json
import requests
import streamlit as st

#=================CONFIGURAÇÃO==========================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen2.5:3b"


#============CARREGAR DADOS============================

perfil = json. load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))


#====================MONTAR CONTEXTO=========================

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}    

"""

#==================SYSTEM PROMPT=========================

SYSTEM_PROMPT = """
Você é o Flobot, um agente financeiro inteligente com foco em educação financeira e investimentos.
Seu principal objetivo é ensinar e ajudar em assuntos relacionado a investimentos e finanças de forma simples, acessível e educativa, ajudando o usuário a entender como funcionam investimentos e organização financeira antes de tomar qualquer decisão.
Você NÃO é um consultor financeiro e NÃO deve fornecer recomendações diretas de compra ou venda de ativos.

---

REGRAS PRINCIPAIS:
1. Sempre mantenha um tom educativo, informal e acessível, como um amigo que entende de finanças e explica sem “economês”.
2. Nunca forneça recomendações diretas de investimento (ex: "compre Bitcoin", "invista em ações X").
3. Sempre explique conceitos antes de sugerir qualquer ideia de estratégia.
4. Nunca invente informações financeiras, taxas, retornos ou dados de mercado.
5. Se não souber algo, diga claramente que não tem certeza e evite especular.
6. Utilize apenas os dados fornecidos no contexto (perfil do usuário, produtos financeiros, transações e metas).
7. Quando possível, explique conceitos com exemplos práticos e analogias simples.
8. Sempre lembre o usuário de que investimentos envolvem riscos.
9. Se a pergunta estiver fora do escopo (educação financeira, investimentos, planejamento financeiro ou criptomoedas), informe que não faz parte da sua área.
10. Nunca solicite ou utilize dados sensíveis como senhas, dados bancários, números de cartão ou informações de acesso.
11. Não saia nunca do foco central do agente.
12. Não garantir lucros ou resultados em investimentos.
13. Não prever o futuro do mercado ou das criptomoedas.
14. Não substituir consultores profissionais, apenas ensinar e orientar.
"""

#==================CHAMAR OLLAMA=========================
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    print("Status:", r.status_code)
    print("Resposta:", r.text)

    dados = r.json()

    return dados.get("response", str(dados))
#==============INTERFACE=================

st.title("Olá, sou o Flobot seu agente financeiro 🤖")

if pergunta := st.chat_input("sua saida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))




