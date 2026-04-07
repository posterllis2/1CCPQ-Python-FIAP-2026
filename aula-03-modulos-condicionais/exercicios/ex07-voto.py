from datetime import date

ano = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
voto = ano_atual - ano

if voto == 18:
    print("Neste ano, seu voto é OBRIGATÓRIO!")
else:
    if 16 < voto < 17:
        print("Neste ano, seu voto é FACULTATIVO!")
    else:
        if voto < 15:
            print("Neste ano, você NÃO pode votar!")
