# Sistema de Gestão de Colheitas - Agronegócio

## Descrição

Este projeto consiste em um sistema desenvolvido em Python para gerenciamento de colheitas no contexto do agronegócio. A aplicação permite ao usuário cadastrar, consultar, atualizar, excluir e analisar dados de produção agrícola, com foco em cálculo de produtividade e perdas.

O sistema foi projetado com dois modos de operação:

- Modo Offline (JSON) → persistência em arquivo  
- Modo Banco de Dados (Oracle) → CRUD completo  

---

## Objetivo

Simular uma solução tecnológica (Agrotech) que auxilia produtores na tomada de decisão, permitindo:

- Controle de produção agrícola  
- Análise de perdas  
- Geração de relatórios  
- Persistência de dados em diferentes formatos  

---

## Contexto do Agronegócio

A produtividade agrícola é medida em toneladas por hectare (t/ha). Durante o processo de colheita, perdas podem ocorrer — especialmente em colheitas mecanizadas — impactando diretamente o resultado financeiro.

O sistema permite calcular:

- Produção total  
- Perdas  
- Produção final  

---

## Funcionalidades

### Modo Offline (JSON)

- Cadastrar colheitas  
- Listar colheitas  
- Gerar relatório  
- Exportar dados  

---

### Modo Banco de Dados (Oracle)

- Cadastrar colheita  
- Listar colheitas  
- Atualizar colheita  
- Deletar colheita  
- Gerar relatório  
- Exportar para JSON  
- Exportar para TXT  

---

## Arquitetura do Sistema

main.py
↓
menu_principal
↓
├── menu_json (modo offline)
└── menu_db (modo banco)
↓
services
↓
Oracle / JSON / TXT / UTILS
---

## Tecnologias Utilizadas

- Python 3  
- Oracle Database (via Docker)  
- Biblioteca `oracledb`  
- Manipulação de arquivos (JSON e TXT)  

---

## Estrutura do Projeto

├── main.py
├── menus/
│ ├── menu_principal.py
│ ├── menu_offline.py
│ └── menu_db.py
├── models/
│ └── colheita.py
├── services/
│ ├── oracle.py
│ ├── json_service.py
│ ├── colheita_service.py
│ ├── utils.py
│ └── txt_service.py
├── data/
│ └── dados.json
├── relatorios/
│ ├── colheitas.json
│ └── colheitas.txt
└── README.md

---

## Regras de Negócio

### Produção Total


produção = hectares × produtividade


### Perda


perda = produção × (perda_percentual / 100)


### Produção Final


produção_final = produção - perda


---

## Conceitos Aplicados

### Subalgoritmos  
Uso de funções com passagem de parâmetros:
- cadastro  
- cálculo de perda  
- geração de relatórios  

---

### Estruturas de Dados  
- Lista → coleção de colheitas  
- Dicionário → representação de colheita  
- Tupla → menu e opções  

---

### Manipulação de Arquivos  
- JSON → armazenamento/exportação  
- TXT → relatórios legíveis  

---

### Banco de Dados (Oracle)  
- Criação de tabela  
- Inserção de dados  
- Consulta  
- Atualização  
- Exclusão  

---

## Docker - Como executar o projeto

### 1. Subir o Oracle com Docker

docker run -d --name oracle-xe -p 1521:1521 -e ORACLE_PASSWORD=oracle gvenzl/oracle-xe

Aguarde até aparecer:

DATABASE IS READY TO USE

2. Criar ambiente virtual
- python3 -m venv venv
- source venv/bin/activate

3. Instalar dependências
- pip install -r requirements.txt

4. Executar o sistema
- python main.py

🔌 Configuração do Banco
- Host: localhost
- Porta: 1521
- Service Name: XEPDB1
- Usuário: system
- Senha: oracle

### Diferenciais do Projeto
- Dois modos de operação (offline e banco)
- Separação em camadas (menus, services, models)
- Código modular e reutilizável
- Interface amigável via terminal
- Integração com banco real (Oracle)

Exemplo de Saída
ID: 1
Tipo: Mecânica
Hectares: 100
Produtividade: 80 t/ha
Produção Total: 8000
Perda: 800
Produção Final: 7200

Conclusão

O sistema demonstra na prática a aplicação de conceitos fundamentais de programação em Python dentro do contexto do agronegócio, integrando lógica de negócio, persistência de dados e organização de código.