from Receita import Receita
from Despesa import Despesa
from menu import menu
from Balanco import Balanco

menu = menu()
opcao = 0

while opcao != 4:
    menu.menuPrincipal()
    opcao = menu.validaInteiro()
    if opcao == 1:
        print('Submenu de Receita')
        receita = Receita()
        print('Qual o valor da receita?')
        valor = menu.validaFloat()
        if valor:
            print('Qual a categoria?')
        catReceita = receita.listaCategoria()

        for i in range(len(catReceita)):
            print(catReceita[i])

        categoriaId = menu.validaInteiro()
        if len(catReceita) >= categoriaId > 0:
            receita.inserirEntrada(valor, opcao, categoriaId)
        else:
            print('Erro! Tente novamente.')
    elif opcao == 2:
        print('Submenu de Despesa')

        print('Qual o valor da despesa?')
        valor = menu.validaFloat()
        if valor:
            despesa = Despesa()

            print('Qual a categoria?')
            catDespesa = despesa.listaCategoria()

            for i in range(len(catDespesa)):
                print(catDespesa[i])

            categoriaId = menu.validaInteiro()
            if len(catDespesa) >= categoriaId > 0:
                despesa.inserirEntrada(valor, opcao, categoriaId)
            else:
                print('Erro! Tente novamente.')
    elif opcao == 3:
        print()
        b = Balanco()
        r = b.receitaTotal()
        d = b.despesaTotal()
        print()
        print('Receitas:', r)
        print('Despesas:', d)
        print('____________________')
        print('Resultado:', b.balancoTotal())
        print()
    elif opcao == 4:
        print('Aplicação encerrada com sucesso!')
        break
    else:
        print('Opção inválida')
