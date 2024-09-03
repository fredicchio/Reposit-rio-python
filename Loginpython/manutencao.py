from banco import banco

def populate_treeview(treeview, data):
    # Primeiro, limpe qualquer dado existente no Treeview
    for item in treeview.get_children():
        treeview.delete(item)

    # Agora, insira os novos dados
    for row in data:
        treeview.insert("", "end", values=row)

class busuarios(object):
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("insert into usuario (nome, telefone, email, usuario, senha) values (?, ?, ?, ?, ?)",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha))
            banco_con.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário: {str(e)}"

    def updateUser(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("update usuario set nome = ?, telefone = ?, email = ?, usuario = ?, senha = ? where idusuario = ?",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario))
            banco_con.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {str(e)}"

    def deleteUser(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("delete from usuario where idusuario = ?", (self.idusuario,))
            banco_con.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário: {str(e)}"

    def selectUser(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("select * from usuario where idusuario = ?", (self.idusuario,))
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
            c.close()
            return "Busca feita com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na busca do usuário: {str(e)}"

    def selectall(self):
        conn = banco()
        try:
            c = conn.conexao.cursor()
            c.execute("select * from usuario")
            rows = c.fetchall()
            c.close()  # Fechar o cursor antes de retornar
            return rows
        except Exception as e:
            print(f"Ocorreu um erro ao buscar os usuários: {str(e)}")
            return []

    
        
class bcidades(object):
    def __init__(self, codcidade=0, nomecid="", estado="", uf=""):
        self.codcidade = codcidade
        self.nomecid = nomecid
        self.estado = estado
        self.uf = uf

    def insertCity(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("insert into cidade (nomecid, estado, uf) values (?, ?, ?)",
                      (self.nomecid, self.estado, self.uf))
            banco_con.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {str(e)}"

    def updateCity(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("update cidade set nomecid = ?, estado = ?, uf = ? where codcidade = ?",
                      (self.nomecid, self.estado, self.uf, self.codcidade))
            banco_con.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração da cidade: {str(e)}"

    def deleteCity(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("delete from cidade where codcidade = ?", (self.codcidade,))
            banco_con.conexao.commit()
            c.close()
            return "Cidade excluída com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão da cidade: {str(e)}"

    def selectCity(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("select * from cidade where codcidade = ?", (self.codcidade,))
            for linha in c:
                self.codcidade = linha[0]
                self.nomecid = linha[1]
                self.estado = linha[2]
                self.uf = linha[3]
            c.close()
            return "Busca feita com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na busca da cidade: {str(e)}"
        
    def selectall(self):
        conn = banco()
        try:
            c = conn.conexao.cursor()
            c.execute("select * from cidade")
            rows = c.fetchall()
            c.close()  # Fechar o cursor antes de retornar
            return rows
        except Exception as e:
            print(f"Ocorreu um erro ao buscar os usuários: {str(e)}")
            return []

class bclientes(object):
    def __init__(self, idcliente=0, nome="", telefone="", email="", codcidade=0):
        self.idcliente = idcliente
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.codcidade = codcidade

    def insertClient(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("INSERT INTO cliente (nome, telefone, email, codcidade) VALUES (?, ?, ?, ?)",
                      (self.nome, self.telefone, self.email, self.codcidade))
            banco_con.conexao.commit()
            c.close()
            return "Cliente cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do cliente: {str(e)}"

    def updateClient(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("UPDATE cliente SET nome = ?, telefone = ?, email = ?, codcidade = ? WHERE idcliente = ?",
                      (self.nome, self.telefone, self.email, self.codcidade, self.idcliente))
            banco_con.conexao.commit()
            c.close()
            return "Cliente atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do cliente: {str(e)}"

    def deleteClient(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("DELETE FROM cliente WHERE idcliente = ?", (self.idcliente,))
            banco_con.conexao.commit()
            c.close()
            return "Cliente excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do cliente: {str(e)}"

    def selectClient(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("SELECT * FROM cliente WHERE idcliente = ?", (self.idcliente,))
            for linha in c:
                self.idcliente = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.codcidade = linha[4]
            c.close()
            return "Busca feita com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na busca do cliente: {str(e)}"

    def getAllCities(self):
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("SELECT codcidade, nomecid FROM cidade")
            cidades = c.fetchall()
            c.close()
            return cidades
        except Exception as e:
            return f"Ocorreu um erro ao buscar as cidades: {str(e)}"   
    
    def selectall(self):
        conn = banco()
        try:
            c = conn.conexao.cursor()
            c.execute("""
                SELECT c.idcliente, c.nome, c.telefone, c.email, ci.nomecid AS cidade
                FROM cliente c
                JOIN cidade ci ON c.codcidade = ci.codcidade
            """)
            rows = c.fetchall()
            print(rows)
            c.close()  # Fechar o cursor antes de retornar
            return rows
        except Exception as e:
            print(f"Ocorreu um erro ao buscar os clientes: {str(e)}")
            return []

class blogin(object):
    def __init__(self, usuario, senha):

        self.usuario = usuario
        self.senha = senha