import sqlite3

def conexao():
    try:
        conn = sqlite3.connect("escola.db")
    except sqlite3.Error as e:
        print(e)
        print("não foi possivel abrir conexao com o banco de dados")
    else:
        cursor = conn.cursor()
        return conn, cursor


def inserir(aluno):
    try:
        sql = ("INSERT INTO aluno (nome, materia, av1, av2, av3, avd, avds, media, situacao)" +
         "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
        conn, cursor = conexao()
        cursor.execute(sql, (aluno.nome, aluno.materia, aluno.av1, aluno.av2, aluno.av3,
            aluno.avd, aluno.avds, aluno.media, aluno.situacao))
        conn.commit()

    except sqlite3.Error as e:
        print(e)
        print("não foi possivel inserir os dados")
    finally:
        cursor.close()
        conn.close()


def alterar(id, aluno):
    try:
        sql = "UPDATE aluno SET nome = ?, materia = ?, av1 = ?, av2 = ?, av3 = ?, avd = ?, \
            avds = ?, media = ?, situacao = ? WHERE id = ?"
        conn, cursor = conexao()
        cursor.execute(
            sql,
            (
                aluno.nome, aluno.materia, aluno.av1, aluno.av2, aluno.av3,
                aluno.avd, aluno.avds, aluno.media, aluno.situacao, id
            )
        )
    except sqlite3.Error as e:
        print("não foi possivel realizar a alteracao")
        print(e)
    else:
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def consultar(id):
    try:
        sql = "SELECT * FROM aluno WHERE id = ?"
        conn, cursor = conexao()
        cursor.execute(sql, (id, ))
    except sqlite3.Error as e:
        print(e)
        print("não foi possivel realizar a consulta")
        cursor.close()
        conn.close()
    else:
        dados = cursor.fetchone()
        cursor.close()
        conn.close()
        return dados


def deletar(id):
    try:
        sql = "DELETE FROM aluno WHERE id = ?"
        conn, cursor = conexao()
        cursor.execute(sql, (id, ))
    except sqlite3.Error as e:
        print(e)
        print("não foi possivel realizar a exclusao")
    else:
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def pesquisar(palavra, situacao):
    try:
        sql = "SELECT * FROM aluno WHERE (nome LIKE ? or materia LIKE ?) AND situacao LIKE ? "
        conn, cursor = conexao()
        cursor.execute(sql, ("%"+str(palavra)+"%", "%"+str(palavra)+"%", "%"+situacao+"%"))
    except sqlite3.Error as e:
        print(e)
        print("não foi possivel realizar a pesquisa")
        cursor.close()
        conn.close()
    else:
        dados = cursor.fetchall()
        cursor.close()
        conn.close()
        return dados


def verTodos():
    try:
        sql = "SELECT * FROM aluno ORDER BY nome"
        conn, cursor = conexao()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
        print("não foi possivel consultar a tabela")
        cursor.close()
        conn.close()
    else:
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows


conn, cursor = conexao()
sql = ("CREATE TABLE IF NOT EXISTS aluno (" +
        "id integer not null primary key autoincrement,"+
        "nome text not null,"+
        "materia text not null," +
        "av1 numeric not null," +
        "av2 numeric not null," +
        "av3 numeric not null," +
        "avd numeric not null," +
        "avds numeric not null," +
        "media numeric not null," +
        "situacao text not null)")
cursor.execute(sql)
cursor.close()
conn.close()