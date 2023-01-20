import sqlite3
from persistencia.bd import BancoDados as bd

class DAOIncidentes:

    def __init__(self, incidente):
        self.Incidente = incidente

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
        conn = sqlite3.connect('bancoIncidentes.db')
        cursor = conn.cursor()
        cursor.execute(f"""
                SELECT * FROM {tabela};
                """)
        dados = cursor.fetchall()

        conn.close()
        return dados
    def lendobdEsp(self, tabela, col,dados):
        conn = sqlite3.connect('bancoIncidentes.db')
        cursor = conn.cursor()
        cursor.execute(f"""
                SELECT * FROM {tabela} WHERE {col} = {dados};
                """)
        dados = cursor.fetchall()

        conn.close()
        return dados

    # alterando os dados da tabela
    def alterandodb(self, tabela, colunaValor, colunaIndicadora, dados):
        conn = sqlite3.connect('bancoIncidentes.db')
        cursor = conn.cursor()
        cursor.execute(f"""
        UPDATE {tabela}
        SET {colunaValor}
        WHERE {colunaIndicadora} = {dados};
        """)
        conn.commit()

        conn.close()

        
    def excluindoInfodb(self, tabela, coluna,valor):
        conn = sqlite3.connect('bancoIncidentes.db')
        cursor = conn.cursor()

        cursor.execute(f"""
        DELETE FROM {tabela}
        WHERE {coluna} like {valor};
        """ ,)

        conn.commit()

        conn.close()
#print(DAOIncidentes.excluindoInfodb(self='self', tabela='Incidente',coluna='idk', valor=2))