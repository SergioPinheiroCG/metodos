"""
Grupo:
Ana Paula Alves Barros
Andre Tadeu Vasconcelos Lins de Barros
Gustavo Tomio Magalhães Kubo
Sérgio Magno Castor Pinheiro
Thiago Limeira de Alencar
Yukio Ferreira Yabuta
"""
from projetoouvidoriabd import *
from operacoesbd import *
import os

opcao = "Abella's Systems"
conexao = abrirBancoDados('localhost','root','88103432','ouvidoria')
while opcao != '5':
    opcao=menu()

    if opcao == '1':
        listarReclamacoes(conexao)

    elif opcao == '2':
        inserirReclamacao(conexao)

    elif opcao == '3':
         removerReclamacao(conexao)


    elif opcao == '4':
        pesquisaReclamacaoCodigo(conexao)

    elif opcao == '5':
                os.system('cls')
                print("")
                print('Muito obrigado por usar o Sistema Ouvidoria. Até logo!')
                print("")

    elif opcao != '5':
        os.system('cls')
        print('Opção inválida. Por favor, escolha uma das opções sugeridas.')
        print("")
        input('Aperte "Enter"" para voltar nas opções. ')
        os.system('cls')

encerrarBancoDados(conexao)