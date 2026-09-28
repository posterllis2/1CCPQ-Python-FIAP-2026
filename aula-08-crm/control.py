from idlelib import query
from pathlib import Path
import json, csv

DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# CREARE / READ / UPDATE / DELETE

# READ
def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

# CREATE
def create_lead(leads_dect):
    leads = read_leads() #Lista
    leads.append(leads_dect)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")
    # CRIAR UMA FORMA PARA NÃO RODAR TODOS OS LEADS QUANDO FORMOS SALVAR UM NOVO


# BUSCAR LEADS COM QUERY
def read_leads_search(query):
    """Busca Leads de acoedo com o query e RETORNA  uma lista de resultadps"""
    leads = read_leads()
    result = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]}". lower()

        if query.lower() in txt_lead:
            result.append((i, lead))

    return result

#EXPORTAR LEADS PARA CSV
def export_csv():
    """Exportar TODOS  os leads para CSV e RETORNA do CSV"""
    path_csv = DATA_DIR / "leads.csv"
    leads = read_leads()

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, leads[0].keys())
            writer.writeheader()
            for row_dict in leads:
                writer.writerow(row_dict)

        return path_csv
    except PermissionError:
        return None
