import abc

from DB import Conexao

class Entrada(abc.ABC):
    db = Conexao()

    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self.__valor = valor
        else:
            print("Valor inválido")

    # Insere Receita ou Despesa

    def inserirEntrada(self, tipoEntrada, thisCategoryId):
        if tipoEntrada == 1:
            self.db.cursor.execute('''INSERT INTO receita(valor, categoria_id) 
                    VALUES (%s, %s)''', (self.valor, thisCategoryId))
        elif tipoEntrada == 2:
            self.db.cursor.execute('''INSERT INTO despesa(valor, categoria_id) 
                    VALUES (%s, %s)''', (self.valor, thisCategoryId))
        else:
            return print("Erro!")
        self.db.conexao.commit()

    # Retorna a soma total dos valores

    def somaTotal(self, tipoEntrada):
        if tipoEntrada == 1:
            self.db.cursor.execute(''' SELECT SUM(VALOR) FROM RECEITA''')
        elif tipoEntrada == 2:
            self.db.cursor.execute(''' SELECT SUM(VALOR) FROM DESPESA''')
        else:
            return print("Erro!")
        result = self.db.cursor.fetchone()
        return result[0]

    # Retorna a soma entre as datas fornecidas

    def somaPorData(self, tipoEntrada, dataInicio, dataFim):
        if tipoEntrada == 1:
            self.db.cursor.execute(''' SELECT SUM(VALOR) FROM receita
                                               WHERE DATA_INSERCAO 
                                               BETWEEN %s AND %s ''', (dataInicio, dataFim))
        elif tipoEntrada == 2:
            self.db.cursor.execute(''' SELECT SUM(VALOR) FROM despesa
                                               WHERE DATA_INSERCAO 
                                               BETWEEN %s AND %s ''', (dataInicio, dataFim))
        else:
            return print("Erro!")
        result = self.db.cursor.fetchone()
        return result[0]

    # Retorna a lista de categorias

    @abc.abstractmethod
    def listaCategoria(self):
        pass
