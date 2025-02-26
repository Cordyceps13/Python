import sqlite3 as sq
import hashlib as hs

# Criação da base de dados e as respetivas tabelas
try:
    db = sq.connect('tarefas.db')
    c = db.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS utilizadores (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome VARCHAR(100) NOT NULL UNIQUE, 
                    password VARCHAR(256) NOT NULL
                    )
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS tarefas (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    tarefa VARCHAR(100) NOT NULL, 
                    data VARCHAR(100) NOT NULL,
                    ID_utilizador INTEGER NOT NULL,
                    FOREIGN KEY (ID_utilizador) REFERENCES utilizadores(ID)
                )
    ''')
    
    # print('Ligado à base de dados \m/') 
    db.commit()
    c.close()

except sq.Error as e:
    print(e)

# Função para criar conexão com a base de dados a ser utilizada em outros ficheiros
def criar_conexao():
    return sq.connect('tarefas.db', check_same_thread=False, timeout=10)

# Função auxiliar para gerar o hash da senha
def Hash(password):
    return hs.sha256(password.encode()).hexdigest()

# Função para inserir utilizadores na base de dados com hash da senha
def signup(conexao, nome, password):
    try:
        password_hash = Hash(password)
        c = conexao.cursor()
        c.execute('INSERT INTO utilizadores (nome, password) VALUES (?, ?)', (nome, password_hash))
        conexao.commit()
        c.close()
        return True
    except sq.Error as e:
        print('Erro ao inserir o utilizador: ', e)
        return False

sessao = None #Variável GLOBAL para armazenar o nome do utilizador com login efetuado
sessao_ID = None #Variável GLOBAL para armazenar o ID do utilizador com login efetuado

# globals()['sessao_ID'] = None
# globals()['sessao'] = None

# Função para verificar o login do utilizador
def Login(conexao, nome, password):
    global sessao_ID #Utilizar a variável global sessao para guardar o ID do utilizador
    global sessao #Utilizar a variável global sessao para guardar o nome do utilizador

    
    password_hash = Hash(password)
    c = conexao.cursor()
    c.execute('SELECT * FROM utilizadores WHERE nome=? AND password=?', (nome, password_hash))
    utilizador = c.fetchone()
    c.close()
    if utilizador:
        sessao_ID = utilizador[0]
        sessao = utilizador[1]
        
        #OUTRA MANEIRA DE UTILIZAR VARIAVEIS GLOBAIS
        # globals()['sessao_ID'] = utilizador[0]
        # globals()['sessao'] = utilizador[1]

# Função para verificar se existe sessão iniciada
def verificar_sessao():
    global sessao
    return bool(sessao) # mesma coisa que a linha de baixo mas mais conciso e mais simples de ler
    # return sessao is not None and sessao != ()

# Função para fazer logout
def destruir_sessao():
    global sessao
    global sessao_ID
    sessao = None
    sessao_ID = None
 
# Função para inserir tarefas na base de dados
def InserirTarefa(conexao, tarefa, data, sessao_ID):
    try:
        c = conexao.cursor()
        c.execute('INSERT INTO tarefas (tarefa, data, ID_utilizador) VALUES (?, ?, ?)', (tarefa, data, sessao_ID))
        conexao.commit()
        c.close()
    except sq.Error as e:
        print('Erro ao inserir a tarefa: ', e)
    
# Função para mostrar as tarefas na base de dados
def VerTarefas(conexao, sessao_ID):
    try:
        c = conexao.cursor()
        c.execute('SELECT ID, tarefa, data FROM tarefas WHERE ID_utilizador=?', (sessao_ID,))
        registos = c.fetchall()
        c.close()
        return registos
    except sq.Error as e:
        print('Erro ao mostrar as tarefas: ', e)
        return[]

# Função para editar tarefas na base de dados
def EditarTarefa(conexao, tarefa_txt, data, edit_task_id):
    try:
        c = conexao.cursor()
        c.execute('UPDATE tarefas SET tarefa=?, data=? WHERE ID=?', (tarefa_txt, data, edit_task_id))
        conexao.commit()
        c.close()
    except sq.Error as e:
        print('Erro ao editar a tarefa: ', e)

# Função para eliminar tarefas na base de dados
def EliminarTarefa(conexao, task_id):
    try:
        c = conexao.cursor()
        c.execute('DELETE FROM tarefas WHERE ID=?', task_id)
        conexao.commit()
        c.close()
    except sq.Error as e:
        print('Erro ao eliminar a tarefa: ', e)
        
        