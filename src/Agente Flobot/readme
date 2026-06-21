# 🤖 Flobot - Agente Financeiro Inteligente

O **Flobot** é um agente financeiro desenvolvido com Python, Streamlit e Ollama, criado com o objetivo de auxiliar usuários na compreensão de conceitos de educação financeira e investimentos de forma simples, acessível e educativa.

Diferente de um consultor financeiro, o Flobot não realiza recomendações diretas de investimento. Seu papel é ensinar, esclarecer dúvidas e incentivar a tomada de decisões conscientes por meio de informações contextualizadas.

---

## 📌 Funcionalidades

- 💬 Chat interativo sobre educação financeira.
- 📊 Utilização do perfil do investidor para personalizar as respostas.
- 📈 Leitura do histórico de transações do usuário.
- 📝 Consulta ao histórico de atendimentos anteriores.
- 💰 Explicação de produtos financeiros disponíveis.
- 🤖 Integração com modelos de linguagem executados localmente via Ollama.
- 🎨 Interface web simples utilizando Streamlit.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Requests
- Ollama
- Modelo Qwen 2.5 (3B)

---

## 📁 Estrutura do Projeto

```
Flobot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   ├── transacoes.csv
│   └── historico_atendimento.csv
│
└── ...
```

---

## ⚙️ Requisitos

- Python 3.10 ou superior
- Ollama instalado
- Modelo Qwen 2.5:3B baixado

---

## 📥 Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Entre na pasta do projeto:

```bash
cd Flobot
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 📦 Baixando o modelo

Após instalar o Ollama, faça o download do modelo utilizado:

```bash
ollama pull qwen2.5:3b
```

Em seguida, inicie o serviço do Ollama caso ele não esteja em execução.

---

## ▶️ Executando o projeto

Execute a aplicação com:

```bash
streamlit .\src\ run app.py
```

A interface será aberta automaticamente no navegador.

---

## 🧠 Como funciona

O Flobot utiliza um modelo de linguagem local hospedado pelo Ollama.

Quando o usuário envia uma pergunta, o sistema:

1. Carrega o perfil do investidor.
2. Lê o histórico de transações.
3. Consulta atendimentos anteriores.
4. Carrega os produtos financeiros disponíveis.
5. Constrói um contexto com essas informações.
6. Envia o contexto juntamente com um *System Prompt* para o modelo de linguagem.
7. Exibe uma resposta educativa e contextualizada ao usuário.

---

## 🎯 Objetivo

Promover a educação financeira por meio de um agente inteligente capaz de explicar conceitos relacionados a:

- Organização financeira
- Investimentos
- Perfil de investidor
- Planejamento financeiro
- Reserva de emergência
- Produtos financeiros
- Criptomoedas (apenas de forma educativa)

Sempre respeitando boas práticas de segurança e sem fornecer recomendações financeiras diretas.

---

## 🔒 Limitações

O Flobot:

- Não realiza consultoria financeira.
- Não prevê o comportamento do mercado.
- Não garante retornos financeiros.
- Não solicita dados sensíveis.
- Atua exclusivamente com fins educacionais.

---

## 👨‍💻 Autor: Carlos Daniel
