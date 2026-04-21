# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">rm570862@fiap.com.br - Renan Seni</a>
- <a href="https://www.linkedin.com/company/inova-fusca">rm569255@fiap.com.br - Caike</a>
- <a href="https://www.linkedin.com/company/inova-fusca">rm570231@fiap.com.br - João Pedro Zavanela Andreu</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">rm572120@fiap.com.br - Jéssica Paula Miranda Gomes</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">rm573086@fiap.com.br- Rafael Briani Rodrigues da Costa</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Tutor</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>


## 📜 Descrição

Este projeto foi desenvolvido no contexto do PBL com o objetivo de aplicar conceitos de programação em Python na resolução de um problema real do agronegócio. O sistema simula uma solução tecnológica (Agrotech) voltada para o gerenciamento de colheitas, permitindo o cadastro, análise e controle de dados relacionados à produção agrícola.

O agronegócio é um dos principais pilares da economia brasileira, envolvendo uma cadeia produtiva complexa que inclui desde o fornecimento de insumos até a distribuição de produtos ao consumidor final. Dentro desse contexto, a produtividade agrícola e a redução de perdas são fatores críticos para garantir eficiência operacional e rentabilidade ao produtor.

A proposta do sistema é auxiliar na análise dessas variáveis, permitindo ao usuário registrar informações como tipo de colheita (manual ou mecânica), área plantada em hectares, produtividade (toneladas por hectare) e percentual de perda. A partir desses dados, o sistema realiza cálculos de produção total, perdas estimadas e produção final, fornecendo informações relevantes para tomada de decisão.

O projeto foi estruturado em dois modos de operação distintos. O primeiro é o modo offline, que utiliza arquivos no formato JSON para persistência de dados. Esse modo permite ao usuário realizar operações básicas como cadastro, listagem e geração de relatórios sem a necessidade de um banco de dados.

O segundo modo utiliza um banco de dados Oracle como fonte principal de dados, permitindo a realização de operações completas de CRUD (Create, Read, Update e Delete). Esse modo também oferece funcionalidades adicionais como atualização e exclusão de registros, além da possibilidade de exportação dos dados para arquivos JSON e TXT.

Durante o desenvolvimento, foram aplicados conceitos fundamentais da disciplina, como subalgoritmos com passagem de parâmetros, estruturas de dados (listas, dicionários e tuplas), manipulação de arquivos e integração com banco de dados. O sistema também foi organizado em camadas (menus, services e models), promovendo melhor separação de responsabilidades e reutilização de código.

Dessa forma, o projeto demonstra na prática como a tecnologia pode ser aplicada no agronegócio para melhorar a gestão da produção, reduzir perdas e apoiar decisões estratégicas.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

### 📌 Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.10 ou superior
- Docker Desktop
- Git (opcional)
- Ambiente virtual (venv)

---

### 🐳 1. Subir o banco Oracle com Docker

Execute o comando abaixo:

bash
docker run -d --name oracle-xe -p 1521:1521 -e ORACLE_PASSWORD=oracle gvenzl/oracle-xe

Aguarde até o banco estar pronto:

DATABASE IS READY TO USE

🐍 2. Clonar o repositório
   git clone <url-do-repositorio>
   cd <nome-do-projeto>
📦 3. Criar e ativar ambiente virtual
Mac/Linux:
   python3 -m venv venv
   source venv/bin/activate
Windows:
   python -m venv venv
   venv\Scripts\activate
📥 4. Instalar dependências
   pip install -r requirements.txt
▶️ 5. Executar o projeto
   python src/main.py
🧭 6. Utilização do sistema

Ao iniciar, o sistema apresentará um menu com duas opções:

Modo Offline (JSON)
Modo Banco de Dados (Oracle)

📂 Modo Offline:
   Dados armazenados em arquivo JSON
   Permite cadastro, listagem e relatórios
🗄️ Modo Banco:
   Dados armazenados no Oracle
   Permite CRUD completo:
   Criar
   Listar
   Atualizar
   Deletar
Exportação para JSON e TXT
🔌 Configuração do banco
   Host: localhost
   Porta: 1521
   Service Name: XEPDB1
   Usuário: system
   Senha: oracle

---
## 🗃 Histórico de lançamentos

* 0.5.0 - 21/04/2026
    * Implementação do modo banco com CRUD completo
    * Integração com Oracle via Docker
    * Exportação para JSON e TXT

* 0.4.0 - 18/04/2026
    * Refatoração da arquitetura (menus, services, models)
    * Separação entre modo offline e banco

* 0.3.0 - 15/04/2026
    * Implementação de geração de relatórios
    * Cálculo de produção, perdas e produção final

* 0.2.0 - 12/04/2026
    * Implementação do modo offline com JSON
    * Cadastro e listagem de colheitas

* 0.1.0 - 10/04/2026
    * Estrutura inicial do projeto
    * Definição do modelo de dados (colheita)

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


