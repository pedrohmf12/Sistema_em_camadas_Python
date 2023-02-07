import sqlite3
from persistencia.bd import BancoDados


class DAOAtendente:
    def cadastrarAtendente(self,cpf,nome,cargo,contratacao,id_endereco):
        try:
            conn = sqlite3.connect('bancoIncidentes.db')
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO Funcionario (nome,cpf, cargo, dt_admissao, id_endereco) VALUES ('{nome}','{cpf}', '{cargo}','{contratacao}', '{id_endereco}');")
            conn.commit()

            conn.close()

            return "Salvo!"
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de atendente: {}".format(e))
            return -1
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return -1
    def cadastrarEndereco(self,logradouro,numero,bairro,complemento,cidade,estado,cep):
        try:
            conn = sqlite3.connect('bancoIncidentes.db')
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO Endereco (logradouro,numero,bairro,complemento,cidade,estadp,cep) VALUES ('{logradouro}','{numero}','{bairro}', '{complemento}', '{cidade}', '{estado}', '{cep}');")
            conn.commit()

            conn.close()

            return "Salvo!"
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de atendente: {}".format(e))
            return -1
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return -1

    # lendo os dados
    def lendobd(self, tabela, dados):

        conn = sqlite3.connect('bancoIncidentes.db')
        cursor = conn.cursor()
        cursor.execute(f"""
        SELECT id_endereco FROM {tabela} WHERE {dados};
        """)
        dados = cursor.fetchall()

        conn.close()
        return dados
