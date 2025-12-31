import sqlite3

# Função para conectar ao banco de dados
def conectar_bd():
    return sqlite3.connect('livros.db')

# Função para criar a tabela se não existir
def criar_tabela():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            genero TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar um livro
def adicionar_livro(titulo, autor, ano, genero):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO livros (titulo, autor, ano, genero) VALUES (?, ?, ?, ?)', 
                   (titulo, autor, ano, genero))
    conn.commit()
    conn.close()
    print("Livro adicionado com sucesso!")

# Função para listar todos os livros
def listar_livros():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conn.close()
    if livros:
        print("\nLista de Livros:")
        for livro in livros:
            print(f"ID: {livro[0]}, Titulo: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Genero: {livro[4]}")
    else:
        print("Nenhum livro encontrado.")

# Função para buscar livro por título
def buscar_livro(titulo):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE titulo LIKE ?', ('%' + titulo + '%',))
    livros = cursor.fetchall()
    conn.close()
    if livros:
        print("\nResultado da Busca:")
        for livro in livros:
            print(f"ID: {livro[0]}, Titulo: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Genero: {livro[4]}")
    else:
        print("Nenhum livro encontrado com esse titulo.")

# Função para atualizar um livro
def atualizar_livro(id_livro, titulo, autor, ano, genero):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('UPDATE livros SET titulo = ?, autor = ?, ano = ?, genero = ? WHERE id = ?',
                   (titulo, autor, ano, genero, id_livro))
    conn.commit()
    conn.close()
    print("Livro atualizado com sucesso!")

# Função para remover um livro
def remover_livro(id_livro):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livros WHERE id = ?', (id_livro,))
    conn.commit()
    conn.close()
    print("Livro removido com sucesso!")

# Função principal com menu
def menu():
    criar_tabela()  # Cria a tabela ao iniciar
    while True:
        print("\n--- Sistema de Gerenciamento de Livros ---")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro por Titulo")
        print("4. Atualizar Livro")
        print("5. Remover Livro")
        print("6. Sair")
        opcao = input("Escolha uma opcao: ")
        
        if opcao == '1':
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            genero = input("Genero: ")
            adicionar_livro(titulo, autor, ano, genero)
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            titulo = input("Digite o titulo para buscar: ")
            buscar_livro(titulo)
        elif opcao == '4':
            id_livro = int(input("ID do livro a atualizar: "))
            titulo = input("Novo Titulo: ")
            autor = input("Novo Autor: ")
            ano = int(input("Novo Ano: "))
            genero = input("Novo Genero: ")
            atualizar_livro(id_livro, titulo, autor, ano, genero)
        elif opcao == '5':
            id_livro = int(input("ID do livro a remover: "))
            remover_livro(id_livro)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opcao invalida!")

# Executar o menu
if __name__ == "__main__":
    menu()