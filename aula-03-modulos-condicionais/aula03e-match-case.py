escolha_usuario = 0
# 0 -> sair do programa
# 1 -> entrar no programa
# >>>> erro!

match escolha_usuario:
        case 0:
            print("Sair do Programa")
        case 1:
            print("Entrar no Programa")
        case _:
            print("ERRO!")