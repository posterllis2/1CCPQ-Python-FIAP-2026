# Dados iniciais fornecidos no exercício
endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

def erros_seguidos(lista_req):
    for i in range(len(lista_req) - 1):
        codigo_atual = lista_req[i]
        prox_codigo = lista_req[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True

    return False

def analisar_endpoint(lista_req):
    qtd_sucesso = 0

    for codigo in lista_req:
        if eh_sucesso(codigo):
            qtd_sucesso += 1

    qtd_req = len(lista_req)
    qtd_erros = qtd_req - qtd_sucesso

    percentual_sucesso = (qtd_sucesso / qtd_req) * 100

    tem_erro_seguidos = erros_seguidos(lista_req)

    if tem_erro_seguidos:
        classificacao = "Crítico"
    elif percentual_sucesso >= 80:
        classificacao = "Estável"
    else:
        classificacao = "Instável"

    return (
        qtd_sucesso,
        qtd_erros,
        percentual_sucesso,
        classificacao
    )

maior_qtd_erros = -1
endpoint_mais_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    status_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(status_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"Percentual de sucesso: {percentual:.1f}%")
    print(f"Classificacao: {classificacao}")
    print("=" * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_mais_erro = nome_endpoint

print(f"Endpoint com mais número de erros é {endpoint_mais_erro} (com {maior_qtd_erros} erros)")