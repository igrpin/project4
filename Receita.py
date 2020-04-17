from Entrada import Entrada

class Receita(Entrada):

    def __init__(self):
        super().__init__()

    # Retorna a soma de receitas em um intervalo de datas

    def consultaReceitasPorData(self, data):
        pass

    # Retorna lista de categorias

    def listaCategoria(self):
        self.db.cursor.execute('''
                    SELECT * FROM categoria_receita''')
        lista = self.db.cursor.fetchall()
        return lista

    # Retorna a soma total de receitas

    def receitaTotal(self):
        self.db.cursor.execute('''SELECT SUM(valor) FROM receita;''')
        return self.db.cursor.fetchone()[0]
