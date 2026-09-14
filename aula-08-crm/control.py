from pathlib import Path
import json
from pydoc import resolve

DATA_DIR = Path(__file__).resolve().parent/ "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR/ "leads.json"

# CRUD
# Create
# Read
def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

print(read_leads())
# Update
# Delete

