import sqlite3

class banco():
    def __init__(self):
        self.conexao = sqlite3.connect('jacinto.db')
        self.createTables()

    def createTables(self):
        c = self.conexao.cursor()
        # Criação da tabela 'usuario'
        c.execute("""
        CREATE TABLE IF NOT EXISTS usuario(
            idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            usuario TEXT,
            senha TEXT
        )
        """)
        
        # Criação da tabela 'cidade'
        c.execute("""
        CREATE TABLE IF NOT EXISTS cidade(
            codcidade INTEGER PRIMARY KEY AUTOINCREMENT,
            nomecid TEXT,
            estado TEXT,
            uf TEXT
        )
        """)
        
        # Criação da tabela 'cliente'
        c.execute("""
        CREATE TABLE IF NOT EXISTS cliente(
            idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            codcidade INTEGER,
            FOREIGN KEY (codcidade) REFERENCES cidade(codcidade)
        )
        """)
        
        self.conexao.commit()
        c.close()
