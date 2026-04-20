import oracledb

def get_connection():
    return oracledb.connect(
        user="system",
        password="oracle",
        dsn="localhost:1521/XEPDB1"
    )
    
def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        BEGIN
            EXECUTE IMMEDIATE '
                CREATE TABLE colheitas (
                    id NUMBER PRIMARY KEY,
                    tipo VARCHAR2(20),
                    hectares NUMBER,
                    produtividade NUMBER,
                    perda_percentual NUMBER
                )
            ';
        EXCEPTION
            WHEN OTHERS THEN
                IF SQLCODE != -955 THEN
                    RAISE;
                END IF;
        END;
    """)

    conn.close()
    
def inserir_colheita(colheita):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO colheitas (id, tipo, hectares, produtividade, perda_percentual)
        VALUES (:1, :2, :3, :4, :5)
    """, (
        colheita["id"],
        colheita["tipo"],
        colheita["hectares"],
        colheita["produtividade"],
        colheita["perda_percentual"]
    ))

    conn.commit()
    conn.close()
    
def listar_colheitas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT ID, TIPO, HECTARES, PRODUTIVIDADE, PERDA_PERCENTUAL FROM colheitas order by id")
    
    cols = [d[0].lower() for d in cursor.description]  # ["id","tipo",...]
    cursor.rowfactory = lambda *args: dict(zip(cols, args))
    
    colheitas = cursor.fetchall()

    conn.close()
    return colheitas

def atualizar_colheita(colheita):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE colheitas
        SET tipo = :1, hectares = :2, produtividade = :3, perda_percentual = :4
        WHERE id = :5
    """, (
        colheita["tipo"],
        colheita["hectares"],
        colheita["produtividade"],
        colheita["perda_percentual"],
        colheita["id"]
    ))

    conn.commit()
    conn.close()

def deletar_colheita(colheita_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM colheitas WHERE id = :1", (colheita_id,))

    conn.commit()
    conn.close()
    
def buscar_colheita_por_id(colheita_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, tipo, hectares, produtividade, perda_percentual FROM colheitas WHERE id = :1",
        (colheita_id,)
    )
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "tipo": row[1],
        "hectares": row[2],
        "produtividade": row[3],
        "perda_percentual": row[4],
    }