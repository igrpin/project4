from Entrada import Entrada
from DB import Conexao


class Receita(Entrada):
    db = Conexao()

    def __init__(self, valor):
        super().__init__(valor)
        print("CRIANDO RECEITA")

    # Retorna a soma de receitas em um intervalo de datas

    def consultaReceitasPorData(self, data):
        pass

    def listaCategoria(self):
        self.db.cursor.execute('''
                    SELECT * FROM categoria_receita''')
        lista = self.db.cursor.fetchall()
        return lista
