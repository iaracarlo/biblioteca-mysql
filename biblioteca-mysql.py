import mysql.connector

# --- CONFIGURAÇÃO DO BANCO DE DADOS ---

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SUA_SENHA',
)
cursor = conexao.cursor()
# Criar o banco caso não exista
cursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca")

# Selecionar o banco
cursor.execute("USE biblioteca")

# Criar a tabela caso não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
)
""")

conexao.commit()

# --- FUNÇÕES DO SISTEMA ---

def cadastrar():
    livro = input('Qual livro deseja cadastrar? ')

    # SQL: Inserir o livro no banco de dados
    cursor.execute(
        "INSERT INTO livros (nome) VALUES (%s)",
        (livro,)
    )
    conexao.commit()

    print('Livro cadastrado com sucesso!')


def buscar():
    busca = input('Qual livro deseja encontrar? ')

    # SQL: Buscar pelo nome do livro
    cursor.execute(
        "SELECT nome FROM livros WHERE nome = %s",
        (busca,)
    )

    resultado = cursor.fetchone()

    if resultado:
        print('Livro encontrado com sucesso!')
    else:
        print('Não encontramos seu livro :/')


def listar():
    # SQL: Selecionar todos os livros cadastrados
    cursor.execute("SELECT nome FROM livros")

    todos_os_livros = cursor.fetchall()

    print('\n=== LISTA DE LIVROS ===')

    if not todos_os_livros:
        print("Nenhum livro cadastrado ainda.")
    else:
        # Loop para mostrar os livros na tela
        for i, linha in enumerate(todos_os_livros):
            print(f'{i + 1} - {linha[0]}')


def trocar():
    troca = input('Qual livro deseja trocar? ')

    # SQL: Verificar se o livro existe antes de trocar
    cursor.execute(
        "SELECT nome FROM livros WHERE nome = %s",
        (troca,)
    )

    if cursor.fetchone():
        livronovo = input(
            f'Qual livro deseja colocar no lugar do {troca}? '
        )

        # SQL: Atualizar o nome do livro antigo pelo novo
        cursor.execute(
            "UPDATE livros SET nome = %s WHERE nome = %s",
            (livronovo, troca)
        )

        conexao.commit()

        print('Livro trocado com sucesso!')
    else:
        print('Não encontramos seu livro em nossa biblioteca!')


def remover():
    removelivro = input('Qual livro deseja remover? ')

    # SQL: Verificar se o livro existe antes de deletar
    cursor.execute(
        "SELECT nome FROM livros WHERE nome = %s",
        (removelivro,)
    )

    if cursor.fetchone():

        # SQL: Deletar o livro pelo nome
        cursor.execute(
            "DELETE FROM livros WHERE nome = %s",
            (removelivro,)
        )

        conexao.commit()

        print('Livro removido com sucesso!')
    else:
        print('Livro não encontrado para remoção!')


# --- MENU PRINCIPAL ---

while True:

    print('\n=== MENU BIBLIOTECA ===')
    print('1 - Cadastrar Livro')
    print('2 - Buscar livro')
    print('3 - Listar livros')
    print('4 - Trocar livro')
    print('5 - Remover livro')
    print('6 - Sair')

    acao = input('O que você deseja fazer? ')

    if acao == '1':
        cadastrar()

    elif acao == '2':
        buscar()

    elif acao == '3':
        listar()

    elif acao == '4':
        trocar()

    elif acao == '5':
        remover()

    elif acao == '6':
        print('Saindo do sistema...')
        break


# Fechar a conexão com o banco de dados
cursor.close()
conexao.close()