nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Parabéns! Aluno Aprovado!")
else:
    if 5 <= media <= 6:
        print("Aluno Em Recuperação!")
    else:
        if media <= 5:
            print("Que pena! Aluno Reprovado")
