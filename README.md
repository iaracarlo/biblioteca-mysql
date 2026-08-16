# 📚 Sistema de Biblioteca

Sistema de gerenciamento de livros desenvolvido em **Python**, utilizando **MySQL** para armazenamento dos dados.

## Tecnologias utilizadas

* Python
* MySQL
* MySQL Connector
* PyCharm

## Funcionalidades:
* **Cadastrar livro** — adiciona um novo livro ao banco de dados.
* **Buscar livro** — verifica se um determinado livro está cadastrado.
* **Listar livros** — exibe todos os livros cadastrados.
* **Trocar livro** — substitui o nome de um livro cadastrado por outro.
* **Remover livro** — remove um livro do banco de dados.
* **Sair** — encerra o sistema.

## 🗄️ Banco de dados

O projeto utiliza o **MySQL** para armazenar os livros.

Ao executar o programa, o banco de dados `biblioteca` é criado automaticamente se você ainda não tiver.

A tabela `livros` possui:

| Campo  | Tipo         | Descrição                    |
| ------ | ------------ | ---------------------------- |
| `id`   | INT          | Identificador único do livro |
| `nome` | VARCHAR(255) | Nome do livro                |

## Para executar o sistema:

### 1. Instale o Python

Veja se o Python está instalado.

### 2. Instale o MySQL

É necessário ter o MySQL instalado e em execução.

### 3. Instale as dependências

No terminal, execute:

```bash
pip install -r requirements.txt
```

### 4. Configure a conexão com o MySQL

No arquivo principal, informe sua senha do MySQL:

```python
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SUA_SENHA',
)
```

### 5. Execute o programa

```bash
python biblioteca-mysql.py
```

## Objetivo do projeto

Este projeto foi desenvolvido para praticar conceitos de **Python, funções, estruturas de repetição, integração com banco de dados MySQL e operações CRUD**.

As operações CRUD praticadas são:

* **Create** → cadastrar livros
* **Read** → buscar e listar livros
* **Update** → trocar livros
* **Delete** → remover livros

## Desenvolvido por

Iara Carvalho
