from re import search

from model import model_lead
import control

def add_lead():
    name = input('Nome:')
    email = input('E-mail:')
    stage = input('Etapa no funil:')

    # valida os dados aqui!!
    # depois de validado, precisamos modelar o lead com um dict
    # para isso, usamos o model
    print(model_lead(name,email,stage))

    # agora...com o meu lead modelado com um dict...
    # precisamos enviar esse lead para leads.json
    # para isso, vamos usar o control
    control.create_lead(model_lead(name,email,stage))

    print('Lead adicionado (func)')

def list_leads():
    leads = control.read_leads()

    print(f'## | {"Nome:":<12} | E-mail')
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead['name']:<12} | {lead['email']}")

def search_leads():
    query = input('Buscar por: ').strip().lower()
    # validra query

    search_results = control.read_leads_search(query)
    print(f'## | {"Nome:":<12} | E-mail')
    for i, lead in search_results:
        print(f"{i:02d} | {lead['name']:<12} | {lead['email']}")

def export_leads():
    path_csv = control.export_csv()
    if path_csv is None:
        print("Não foi possível exportar para CSV")
    else:
        print(f"Exportado para {path_csv}")

# +1 desafio: formatar como tabela

def main():
    while True:
        print('/nMini CRM de Leads')
        print('[1] Adicionar lead')
        print('[2] Listar leads')
        print('[3] Buscar (nome/e-mail)')
        print('[4] Exportar para CSV')
        print('[0] Sair do progrma')

        opt = input('Escolha uma opções')

        if opt == '1':
            add_lead()
        elif opt == '2':
            list_leads()
        elif opt == '3':
            search_leads()
        elif opt == '4':
            export_leads()
        elif opt == '0':
            print('Até mais...')
            break
        else:
            print('Opções inválida')


if __name__ == '__main__':
    main()
