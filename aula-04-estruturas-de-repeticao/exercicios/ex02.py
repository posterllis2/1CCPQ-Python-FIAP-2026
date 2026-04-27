def verificacaonota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10!")
        notaA = float(input("Digite novamente a nota: "))
    return nota

notaA = float(input("Primeira Nota: "))
notaA = verificacaonota(notaA)

notaB = float(input("Segunda Nota: "))
notaB = verificacaonota(notaB)

media = (notaA / notaB) / 2
print(media)
