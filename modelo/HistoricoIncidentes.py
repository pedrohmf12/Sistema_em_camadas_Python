from persistencia.DAOIncidenteP import DAOIncidentes
from visao.HistoricoIncidentesView import *

class HistoricoIncidentes:

    def __init__(self):
        self.prioridade = ""
        self.codigo = ""
        self.data = ""
        self.nome_cliente = ""

    @property
    def prioridade(self):
        return self._prioridade

    @prioridade.setter
    def prioridade(self, value):
        self._prioriodade = value


    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value


    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


    @property
    def nome_cliente(self):
        return self._nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, value):
        self._nome_cliente = value

    # def consultar_nome(self):
    #     dao = DAOIncidentes(self)
    #     return dao.lendobdEsp(self,'Cliente','nome')
    #
    # def consultar_codigo(self):
    #     dao = DAOIncidentes(self)
    #     return dao.lendobdEsp(self,'Incidente','idk')
    #
    # def consultar_data(self):
    #     dao = DAOIncidentes(self)
    #     return dao.lendobdEsp(self,'Incidente','dt_registro')



