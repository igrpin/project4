from Receita import Receita
from Despesa import Despesa
from menu import menu

menu = menu()
opcao = 0

while opcao != 4:
    menu.menuPrincipal()
    opcao = menu.validaInteiro()
    if opcao == 1:
        print('Submenu de Receita')

        print('Qual o valor da receita?')
        valor = menu.validaFloat()
        if valor:
            receita = Receita(valor)

            print('Qual a categoria?')
            catReceita = receita.listaCategoria()

            for i in range(len(catReceita)):
                print(catReceita[i])

            categoriaId = menu.validaInteiro()
            if len(catReceita) >= categoriaId > 0:
                receita.inserirEntrada(1, categoriaId)
            else:
                print('Erro! Tente novamente.')
    elif opcao == 2:
        print('Submenu de Despesa')
    elif opcao == 3:
        print('Submenu de balanço')
    elif opcao == 4:
        print('Aplicação encerrada com sucesso!')
        break
    else:
        print('Opção inválida')