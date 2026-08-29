import conexao_sql

def criar_tabela():
    """Cria a tabela contatos caso ela ainda não exista."""
    conn = conexao_sql.conectar()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            nome     VARCHAR(100) PRIMARY KEY,
            telefone VARCHAR(20) NOT NULL,
            email    VARCHAR(100)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def adicionar(nome, telefone, email):

    """Insere um novo contato. Retorna True se deu certo, False se o nome já existe."""

    conn = conexao_sql.conectar()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)",
            (nome, telefone, email)
        )
        conn.commit()
        return True
    
    except conexao_sql.psycopg2.errors.UniqueViolation:
        conn.rollback()
        return False
    
    finally:
        cur.close()
        conn.close()  

def buscar(nome):
    conn = conexao_sql.conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contatos WHERE nome ILIKE %s", (f"%{nome}%",))
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    print(resultado)

def contato_existe(nome):
    #Verifica se um contato com nome exato já existe.
    conn = conexao_sql.conectar()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM contatos WHERE nome = %s", (nome,))
    existe = cur.fetchone() is not None
    cur.close()
    conn.close()
    print(existe)

def editar(nome, telefone=None, email=None):
    
    conn = conexao_sql.conectar()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE contatos
        SET telefone = COALESCE(%s, telefone),
            email    = COALESCE(%s, email)
        WHERE nome = %s
        """,
        (telefone, email, nome)
    )
    linhas_afetadas = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return linhas_afetadas > 0

def listar():
    conn = conexao_sql.conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contatos")
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    print(resultado)

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