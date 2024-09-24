import mysql.connector
from mysql.connector import Error

def cb():
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'escola3'
        )
        if conn.is_connected():
            print('Conexão bem sucedida')
            return conn, conn.cursor()
    except Error as e:
        print(f"Erro ao conectar ao banco de dados : {e}")
        return None, None
    
def fc(conn, cursor):
    if cursor is not None:
        cursor.close()
    if conn is not None and conn.is_connected():
        conn.close()
        print('Conexão encerrada')

def main():
    conn, cursor = cb()
    if conn is not None and cursor is not None:
        try:
            nome = input('digite o seu nome de usuario: ')
            senha = input('digite sua senha: ') 

            sql = "INSERT INTO tbl_usuarios (nome, username, senha) VALUES ('teste',%s, %s)"
            val = (nome, senha)

            cursor.execute(sql,val)
            conn.commit()

            print('deu certo')

        except Error as e:
            print(f"Erro ao conectar ao banco de dados : {e}")
        finally:
            fc(conn, cursor)

if __name__ == "__main__":
    main()