# nome["chave"] = "valor" --> chave + valor se chama intem

# Fazendo o dicionário
eng2sp = dict()

eng2ss = {
    "one": "uno",
    "two": "dois",
    "three": "tres"
}
# dá pra usar a chave para achar o valor
print(eng2ss["two"])

# Operador in (retorna se é V ou F)
print("uno" in eng2ss)

#Selecionar valores
valores = eng2ss.values()
print("one" in valores)