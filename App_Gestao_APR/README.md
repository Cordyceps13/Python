# AUTOR: ANDRÉ MANUEL DIAS PROENÇA

# UFCD_10790 - Projeto de Programação

--------------------------------------------------------------------------------------------------

# Aplicação de gestão pessoal (Lista de tarefas)

Uma aplicação simples, para gestão pessoal que permite adicionar, 
editar e eliminar tarefas, com ambiente gráfico desenvolvida em Flet, 
uma framework de Python.

--------------------------------------------------------------------------------------------------

## Índice

- [Introdução](#introdução)
- [Âmbito do Projeto](#âmbito-do-projeto)
- [Levantamento de Requisitos](#levantamento-de-requisitos)
- [Elaboração do Projeto](#elaboração-do-projeto)
- [Desempenho do Projeto](#desempenho-do-projeto)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Resultados](#resultados)
- [Conclusão](#conclusão)
- [Trabalhos Futuros](#trabalhos-futuros)

--------------------------------------------------------------------------------------------------

## Introdução

Este projeto consiste numa aplicação com ambiente gráfico para gestão pessoal, 
criação e listagem de tarefas (to dos)
A aplicação possui funcionalidades para criar, listar, editar e eliminar tarefas
e também permite a inserção de utilizadores na base de dados e efetuar login, de modo
a serem mostradas apenas as tarefas criadas pelo utilizador autenticado

--------------------------------------------------------------------------------------------------

## Âmbito do Projeto

- **Objetivo**: 

  - Desenvolver uma aplicação com ambiente gráfico para ajudar na gestão pessoal


- **Objetivos Específicos**:

  - Implementar funcionalidades CRUD (Create, Read, Update and Delete)
  - Utilizar uma base de dados simples para armazenamento das tarefas criadas e associá-las ao utilizador (SQLite).


- **Público-Alvo**: 
  
  - Eu mesmo
  - Pessoas distraídas e/ou com TDAH


- ## **Limitações**:
  
  - Conhecimento do framework
  - Tempo limitado para aquisição de conhecimentos e a sua implementação
  - Framework relativamente recente, o que limita os recursos de informação 

--------------------------------------------------------------------------------------------------

## Levantamento de Requisitos

### Requisitos Funcionais

- **RF01**: A aplicação deve permitir adicionar tarefas
- **RF02**: A aplicação deve listar as tarefas adicionadas
- **RF03**: "     "      "  permitir editar as tarefas adicionadas
- **RF04**: "     "      "  permitir apagar as tarefas concluídas
- **RF05**: "     "      "  gerir as tarefas na base de dados e associá-las ao utilizador que as criou

--------------------------------------------------------------------------------------------------

### Requisitos Não Funcionais

- **RNF01**: Python 3.11.7
- **RNF02**: Flet (Flutter para Python)
- **RNF03**: Biblioteca Datetime
- **RNF04**: Base de dados SQLite3

--------------------------------------------------------------------------------------------------

## Elaboração do Projeto

### Arquitetura

A arquitetura da aplicação é dividida em ..

  - **Front-End**: Interface gráfica (GUI) para facilitar a interação com o utilizador.
  - **Back-End**: Gestão das tarefas adicionadas/editadas/eliminadas na base de dados

--------------------------------------------------------------------------------------------------

### Tecnologias Utilizadas

- **Linguagens**: 

  - Python 3.11.7
  - Framework Flet (Flutter para Python)
  - SQL

--------------------------------------------------------------------------------------------------

- **Bibliotecas**:

  - **flet**: Para criar ambiente gráfico para interagir com o utilizador
  - **datetime**: Para adicionar a data em que as tarefas são criadas
  - **sqlite3**: Para operações com a base de dados.
  - **hashlib**: Para armazenar passwords encriptadas
  - **time**: Utilizada para criar tempo de espera entre eventos
  - **sys**: Utilizada para encerrar a execução da aplicação

--------------------------------------------------------------------------------------------------

- **Ferramentas**:

  - GitHub para controlo de versão.
  - Visual Studio Code como IDE.
  - ChatGpt para esclarecimento de dúvidas.

--------------------------------------------------------------------------------------------------

### Implementação

#### Ficheiros

  #Ficheiro para criação da base de dados que contém as funções com Queries de manipulação da mesma

	- database.py

		##Funções
			- criar_conexão() -> Efetua a ligação da app à base de dados
			- Hash(password) -> Gera o hash das passwords
			- signup(conexao, nome, password) -> Insere utilizadores na base de dados com hash de password
			- login(conexao, nome, password) -> Efetua o login dos utilizadores
			- verificar_sessao() -> Verifica se existe alguma sessão iniciada
			- destruir_sessao() -> Efetua o logout do utilizador
			- InserirTarefa(conexao, tarefa, data, ID_utilizador) -> Faz a inserção de tarefas na base de dados
			- VerTarefas(conexao, sessao_ID) -> Lista as tarefas na app dependendo do utilizador
			- EditarTarefa(conexao, tarefa_txt_, data, edit_task_id) -> Permite a edição de tarefas existentes na base de dados
			- EliminarTarefa(conexao, task_id) -> Elimina tarefas da base de dados com base no ID passado por argumento

  #Ficheiro que contém a base de dados local

	- tarefas.db

  #Ficheiro que contém o módulo da lista de tarefas

	- to_do.py

		##Funções
			- abrir_lista_tarefas(page: ft.Page) -> Permite abrir o módulo quando chamada em outros ficheiros
			- voltar() -> Permite voltar à página inicial

  #Ficheiro que contém o container das tarefas

	- container_tarefa.py

		##Classe
			- Tarefa(ft.UserControl) -> Utilizada para criar o container de cada tarefa

		##Funções
			- rasurar_texto(self, e) -> Marca a tarefa como concluída quando é clicada a respetiva checkbox
			- ApagarEditarTarefas(self, name, color, func) -> Associa a ação dos botões consoante aquele que é clicado

  #Ficheiro que contém a página de registo de utilizadores

	- singup.py

		##Funções
			- abrir_signup(page: ft.Page) -> Permite abrir o módulo quando chamada em outros ficheiros
			- voltar(e) -> Permite voltar à página principal
			- fechar_alert(page) -> Maior controle para fechar o AlertDialog
			- ir_para_login() -> Navegar para a página de login após registo efetuado com sucesso

  #Ficheiro que contém a página de login

	- login.py

		##Funções
			- abrir_login(page: ft.Page) -> Permite abrir o módulo quando chamada em outros ficheiros
			- voltar(e) -> Permite voltar à página principal
			- fechar_alert(page) -> Maior controle para fechar o AlertDialog

  #Ficheiro principal da aplicação

	- main.py

		##Funções
			- fechar_app(e) -> Permite terminar por completo a execução da aplicação

  #Ficheiro com as dependências do projeto

	- requirements.txt

--------------------------------------------------------------------------------------------------

## Desempenho do Projeto

### Testes Realizados

- **Testes funcionais**: 

  - Verificar a possibilidade de adicionar tarefas
	- prints no try/except para depuração através do terminal
	- abrir ficheiro da base de dados na app DB Browser para garantir a inserção

  - Verificar se as tarefas são listadas após serem adicionadas
	- navegar até à página das tarefas na aplicação para verificar se estão a ser listadas

  - Verificar a possibilidade de editar as tarefas adicionadas
	- prints no try/except para depuração através do terminal
	- abrir ficheiro da base de dados na app DB Browser para garantir que a edição foi efetuada

  - Verificar a possibilidade de eliminar as tarefas adicionadas
	- prints no try/except para depuração através do terminal
	- abrir ficheiro da base de dados na app DB Browser para garantir que a tarefa foi eliminada

  - Testar se o registo de utilizadores é efetuado com sucesso
	- prints no try/except para depuração através do terminal
	- abrir ficheiro da base de dados na app DB Browser para garantir que o utilizador foi inserido com sucesso

  - Testar o login 
	- print de cada variável para garantir que chegam dados 
	- print após a query para depuração através do terminal

  - Verificar se as tarefas são associadas a cada utilizador
	- efetuar login com determinado utilizador e verificar na pagina de listagem de tarefas
	  se as tarefas listadas são as mesmas que foram criadas por esse utilizador
	- abrir ficheiro da base de dados na app DB Browser para verificar se o ID do utilizador
	  foi associado à tarefa criada por ele

  - Testar navegação entre páginas/módulos
	- navegar entre páginas/módulos para garantir que a navegação ocorre sem erros

--------------------------------------------------------------------------------------------------

## Como Executar o Projeto

```bash
# Clonar o repositório

  - git clone https://github.com/Cordyceps13/Python.git

# Navegar até ao diretório do projeto

  - cd Python\App_Gestao_APR
	

```Terminal do IDE

# Criar ambiente virtual

  - python -m venv venv


# Instalar as dependências

  - pip install -r requirements.txt


# Executar a applicação

  - python main.py

```

--------------------------------------------------------------------------------------------------

## Conclusão

	Este projeto veio-me mostrar que ainda tenho muito para aprender na construção de aplicações funcionais