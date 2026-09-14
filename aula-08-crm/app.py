from model import model_lead

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    stage = input("Stage: ")

    # Validar dados

    # Depois de validado, precisamos modelar o lead como dict
    # para isso, usamos model
    print(model_lead(name,email,stage))

    # Com meu Lead modelado como Dict preciso enviar esse lead para
    # o leads.json, para isso vamos usar o control
    

    print("Lead adicionado com sucesso!")

def main():
    while True:
        print("/nCRM de Leads")
        print("[1] Adicionar Lead")
        print("[2] Lista de Leads")
        print("[0] Sair do Programa")

        opt = input("Escolha sua opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            print("Lista de Leads")
        elif opt == "0":
            print("Sair do Programa")
            break
        else:
            print("Opção Invalida!")
