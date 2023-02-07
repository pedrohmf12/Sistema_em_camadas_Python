import sqlite3
from persistencia.bd import BancoDados as bd

class DAOIncidentes:

    # Inserindo dados
    def inserirdbIncidente(self, d1,d2,d3,d4):
        try:
            conn = sqlite3.connect('bancoIncidentes.db')
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO Incidente (grau, cpf, dt_registro, status) VALUES ('{d1}','{d2}','{d3}', '{d4}');")
            conn.commit()

            conn.close()
        except sqlite3.OperationalError as e:
            print("Erro na execução do SQL: {}".format(e))
            return (-1)
    # Inserindo dados
    def inserirdb(self, tabela, colunas, dados):
        try:
            conn = bd()
            cursor = conn.cursor()

            cursor.execute(f"""
            INSERT INTO {tabela} ({colunas})
            VALUES ({dados})
            """)
            conn.commit()

            conn.close()
        except sqlite3.OperationalError as e:
            print("Erro na execução do SQL: {}".format(e))
            return (-1)

    # lendo os dados
    def lendobd(self, tabela):
        try:
            dados = []
            conn = bd()
            cursor = conn.cursor()
            cursor.execute(f"""
            SELECT * FROM {tabela};
            """)

            for linha in cursor.fetchall():
                dados.append(linha)
            conn.close()
            return dados
        except sqlite3.OperationalError as e:
            print("Erro na execução do SQL: {}".format(e))
    # lendo linha especifica db
    def lendobdEsp(self, tabela, coluna, dado):
        try:
            dados = []
            conn = bd()
            cursor = conn.cursor()
            cursor.execute(f"""
                    SELECT * FROM {tabela} WHERE {coluna} = {dado};
                    """)
            linha = cursor.fetchall()
            conn.close()

            return linha
        except sqlite3.OperationalError as e:
            print("Erro na execução do SQL: {}".format(e))

    # alterando os dados da tabela
    def alterandodb(self, tabela, colunaValor, colunaIndicadora, dados):
        conn = bd()
        cursor = conn.cursor()
        cursor.execute(f"""
        UPDATE {tabela}
        SET {colunaValor}
        WHERE {colunaIndicadora} = {dados};
        """)
        conn.commit()

        conn.close()
    def excluindoInfodb(self, tabela, colunaValor):
        conn = bd()
        cursor = conn.cursor()

        cursor.execute(f"""
        DELETE FROM {tabela}
        WHERE {colunaValor};
        """ ,)

        conn.commit()

        conn.close()
