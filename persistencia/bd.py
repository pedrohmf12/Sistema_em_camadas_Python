import sqlite3

class BancoDados():
    #Verifica se possui algum banco criado, caso não tenha cria um
    def criarbd(self):
        try:
            conn = sqlite3.connect('bancoIncidentes.db')
            cursor = conn.cursor()
            #Cria cada tabela
            cursor.execute("""
            CREATE TABLE Endereco (
                    id_endereco INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    numero CHAR(50) NOT NULL,
                    complemento CHAR(50) NOT NULL,
                    cep CHAR(10)NOT NULL,
                    logradouro CHAR(50) NOT NULL,
                    bairro CHAR(50) NOT NULL,
                    cidade CHAR(50) NOT NULL,
                    estadp CHAR(50) NOT NULL
            );""")
            cursor.execute("""
            CREATE TABLE Cliente (
                    idk INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome CHAR(30) NOT NULL,
                    cpf CHAR(14) NOT NULL,
                    telefone CHAR(14)NOT NULL,
                    id_endereco INTEGER NOT NULL,
                    FOREIGN KEY (id_endereco) REFERENCES Endereco (id_endereco)
            );
            """)
            cursor.execute("""
            CREATE TABLE Incidente (
                    idk INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    grau CHAR(14) NOT NULL,
                    cpf CHAR(14) NOT NULL,
                    dt_registro CHAR(10) NOT NULL,
                    status TEXT NOT NULL
            );
            """)
            cursor.execute("""
            CREATE TABLE Funcionario (
                    idk INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome CHAR(30) NOT NULL,
                    cpf CHAR(14) NOT NULL,
                    id_endereco INTEGER NOT NULL,
                    cargo CHAR(20) NOT NULL,
                    dt_admissao CHAR(20) NOT NULL,
                    FOREIGN KEY (id_endereco) REFERENCES Endereco (id_endereco)
            );
            """)
            conn.close()
        except:pass

    # Inserindo dados
    def inserirdb(self, tabela, colunas, dados):

        conn = sqlite3.connect('incidentes/bancoIncidentes.db')
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {tabela} ({colunas}) VALUES ({dados});")
        conn.commit()

        conn.close()

    #lendo os dados
    def lendobd(self, tabela):
        dados = []
        conn = sqlite3.connect('incidentes/bancoIncidentes.db')
        cursor = conn.cursor()
        cursor.execute(f"""
        SELECT * FROM {tabela};
        """)

        for linha in cursor.fetchall():
            dados.append(linha)
        conn.close()
        return dados

    # lendo linha especifica db
    def lendobdEsp(self, tabela, coluna, dado):
        dados = []
        conn = sqlite3.connect('incidentes/bancoIncidentes.db')
        cursor = conn.cursor()
        cursor.execute(f"""
                SELECT * FROM {tabela} WHERE {coluna} = {dado};
                """)
        linha = cursor.fetchall()
        conn.close()

        return linha
    # alterando os dados da tabela
    def alterandodb(self, tabela, colunaValor, colunaIndicadora, dados):
        conn = sqlite3.connect('incidentes/bancoIncidentes.db')
        cursor = conn.cursor()
        cursor.execute(f"""
        UPDATE {tabela}
        SET {colunaValor}
        WHERE {colunaIndicadora} = {dados};
        """)
        conn.commit()

        conn.close()
    def excluindoInfodb(self, tabela, colunaValor):
        conn = sqlite3.connect('incidentes/bancoIncidentes.db')
        cursor = conn.cursor()

        cursor.execute(f"""
        DELETE FROM {tabela}
        WHERE {colunaValor};
        """,)

        conn.commit()

        conn.close()

BancoDados.criarbd(self='self')





