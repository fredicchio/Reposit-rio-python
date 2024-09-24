from banco import cb, fc

# Função para selecionar cidades
def select_cidades():
    conn, cursor = cb()
    cidades = []
    try:
        cursor.execute("SELECT * FROM tbl_cidades")
        cidades = cursor.fetchall()
    except Exception as e:
        print(f"Erro ao buscar cidades: {e}")
    finally:
        fc(conn, cursor)
    return cidades

# Função para adicionar uma cidade
def add_cidade(nome, uf):
    conn, cursor = cb()
    try:
        sql = "INSERT INTO tbl_cidades (Nome, UF) VALUES (%s, %s)"
        val = (nome, uf)
        cursor.execute(sql, val)
        conn.commit()
    except Exception as e:
        print(f"Erro ao adicionar cidade: {e}")
    finally:
        fc(conn, cursor)

# Função para deletar uma cidade
def delete_cidade(cidade_id):
    conn, cursor = cb()
    try:
        sql = "DELETE FROM tbl_cidades WHERE CID_COD = %s"
        cursor.execute(sql, (cidade_id,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao deletar cidade: {e}")
    finally:
        fc(conn, cursor)

# Função para atualizar uma cidade
def update_cidade(cidade_id, nome, uf):
    conn, cursor = cb()
    try:
        sql = "UPDATE tbl_cidades SET Nome = %s, UF = %s WHERE CID_COD = %s"
        cursor.execute(sql, (nome, uf, cidade_id))
        conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar cidade: {e}")
    finally:
        fc(conn, cursor)

# Funções para selecionar usuários
def select_usuarios():
    conn, cursor = cb()
    usuarios = []
    try:
        cursor.execute("SELECT * FROM tbl_usuarios")
        usuarios = cursor.fetchall()
    except Exception as e:
        print(f"Erro ao buscar usuários: {e}")
    finally:
        fc(conn, cursor)
    return usuarios

# Função para adicionar um usuário
def add_usuario(nome, username, senha):
    conn, cursor = cb()
    try:
        sql = "INSERT INTO tbl_usuarios (nome, username, senha) VALUES (%s, %s, %s)"
        val = (nome, username, senha)
        cursor.execute(sql, val)
        conn.commit()
    except Exception as e:
        print(f"Erro ao adicionar usuário: {e}")
    finally:
        fc(conn, cursor)

# Função para deletar um usuário
def delete_usuario(usuario_id):
    conn, cursor = cb()
    try:
        sql = "DELETE FROM tbl_usuarios WHERE Id = %s"
        cursor.execute(sql, (usuario_id,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
    finally:
        fc(conn, cursor)

# Função para atualizar um usuário
def update_usuario(usuario_id, nome, username, senha):
    conn, cursor = cb()
    try:
        sql = "UPDATE tbl_usuarios SET nome = %s, username = %s, senha = %s WHERE Id = %s"
        cursor.execute(sql, (nome, username, senha, usuario_id))
        conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
    finally:
        fc(conn, cursor)
