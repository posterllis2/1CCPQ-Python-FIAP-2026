def  contador_letras(palavra):
    dicionario = dict()
    for letra in palavra:
        if letra not in dicionario:
            dicionario[letra] = 1
        else:
            dicionario[letra] += 1
    return dicionario

dict_contagem = contador_letras("Paralelepipedo")
print(dict_contagem)