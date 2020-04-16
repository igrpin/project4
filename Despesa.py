from Entrada import Entrada


class Despesa(Entrada):
    def __init__(self, valor):
        super().__init__(valor)
        print("CRIANDO DESPESA")

    def listaCategoria(self):
        self.db.cursor.execute('''
                            SELECT * FROM categoria_despesa''')
        lista = self.db.cursor.fetchall()
        return lista