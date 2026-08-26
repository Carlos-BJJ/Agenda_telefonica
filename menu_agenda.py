import conexao_sql

def adicionar(nome, telefone, email):

    conn = conexao_sql.conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)",
        (nome, telefone, email))
    conn.commit()
    conn.close()  
    cur.close()  

def buscar(nome):
    conn = conexao_sql.conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contatos WHERE nome ILIKE %s", (f"%{nome}%",))
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado

def editar(nome, telefone, email):
    conn = conexao_sql.conectar()
    cur = conn.cursor()
    cur.execute("UPDATE ... SET ... WHERE")
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado

def listar():
    conn = conexao_sql.conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contatos")
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado

def remover(nome):
    """Remove um contato pelo nome. Retorna True se removeu, False se não existia."""
    conn = conexao_sql.conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM contatos WHERE nome = %s", (nome,))
    linhas_afetadas = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return linhas_afetadas > 0