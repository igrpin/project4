from Receita import Receita
from Despesa import Despesa


class Balanco(Receita, Despesa):

    def balancoTotal(self):
        return self.receitaTotal() - self.despesaTotal()
