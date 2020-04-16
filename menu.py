from DB import Conexao


class menu:
    db = Conexao()

    def menuPrincipal(self):
        print('1 - Inserir Receita')
        print('2 - Inserir Despesa')
        print('3 - Balanço')
        print('4 - Sair')

    def validaInteiro(self):
        try:
            value = int(input('==> '))
            return value
        except ValueError:
            print('**** Digite uma opção válida ****')
            return False

    def validaFloat(self):
        try:
            valor = float(input('==>'))
            return valor
        except ValueError:
            print('**** Valor inválido ****')
            return False

    def validaOpcaoMenuPrincipal(self, validaOpcao):
        while not validaOpcao:
            self.menuPrincipal()
            validaOpcao = self.validaInteiro()
        return validaOpcao

    def subMenuReceita(self):
        pass
