from Entrada import Entrada


class Despesa(Entrada):

    def __init__(self):
        super().__init__()

    def consultaDespesasPorData(self, data):
        pass

    def listaCategoria(self):
        self.db.cursor.execute('''SELECT * FROM categoria_despesa''')
        lista = self.db.cursor.fetchall()
        return lista

    def despesaTotal(self):
        self.db.cursor.execute(''' SELECT SUM(VALOR) FROM despesa''')
        return self.db.cursor.fetchone()[0]