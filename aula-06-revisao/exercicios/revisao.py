# Dados iniciais fornecidos no exercício
endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]


# Função auxiliar para checar se um código é sucesso
def eh_sucesso(codigo):
    return 200 <= codigo <= 299


# 1. Função para contar sucessos e erros
def contar_resultados(requisicoes):
    sucessos = sum(1 for req in requisicoes if eh_sucesso(req))
    erros = len(requisicoes) - sucessos
    return sucessos, erros


# 1. Função para calcular o percentual de sucesso
def calcular_percentual_sucesso(sucessos, total):
    if total == 0:
        return 0
    return (sucessos / total) * 100


# 2. Função para identificar o endpoint com mais erros
def identificar_endpoint_mais_erros(lista_endpoints, matriz_status):
    max_erros = -1
    endpoint_pior = ""

    for i in range(len(lista_endpoints)):
        _, erros = contar_resultados(matriz_status[i])
        if erros > max_erros:
            max_erros = erros
            endpoint_pior = lista_endpoints[i]

    return endpoint_pior, max_erros


# 3. Função para verificar se houve dois erros seguidos
def verificar_erros_consecutivos(requisicoes):
    for i in range(len(requisicoes) - 1):
        if not eh_sucesso(requisicoes[i]) and not eh_sucesso(requisicoes[i + 1]):
            return True
    return False


# 4. Função para classificar o endpoint
def classificar_endpoint(percentual, tem_erros_consecutivos):
    if tem_erros_consecutivos:
        return "CRÍTICO"
    elif percentual >= 80:
        return "ESTÁVEL"
    else:
        return "INSTÁVEL"


# Função principal para gerar o relatório no formato exigido
def gerar_relatorio(lista_endpoints, matriz_status):
    print("--- RELATÓRIO DE ENDPOINTS ---\n")

    for i in range(len(lista_endpoints)):
        endpoint = lista_endpoints[i]
        requisicoes = matriz_status[i]
        total_reqs = len(requisicoes)

        # Chamando as funções que criamos
        sucessos, erros = contar_resultados(requisicoes)
        percentual = calcular_percentual_sucesso(sucessos, total_reqs)
        erros_consecutivos = verificar_erros_consecutivos(requisicoes)
        classificacao = classificar_endpoint(percentual, erros_consecutivos)

        # Exibindo os resultados no formato solicitado
        print(f"Endpoint: {endpoint}")
        print(f"Sucessos: {sucessos}")
        print(f"Erros: {erros}")
        print(f"Percentual: {percentual:.0f}%")
        print(f"Classificação: {classificacao}")
        print("-" * 30)

    # Exibindo o endpoint com mais erros ao final
    pior_endpoint, qtd_erros = identificar_endpoint_mais_erros(lista_endpoints, matriz_status)
    print(f"\n=> O endpoint com mais erros foi '{pior_endpoint}' com {qtd_erros} erros.")


# Executando o código
gerar_relatorio(endpoints, status)