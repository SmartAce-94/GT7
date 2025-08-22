import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

print("🔍 Début du scraping Fandom...")

url = "https://gran-turismo.fandom.com/wiki/Sport_Mode_(GT7)/Daily_Races"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"❌ Erreur HTTP : {response.status_code}")
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")

# Utilisation de select() pour plus de fiabilité
tables = soup.select("table.wikitable")
print(f"📊 Nombre de tableaux trouvés : {len(tables)}")

if not tables:
    print("⚠️ Aucun tableau trouvé. Le format de la page a peut-être changé.")
    exit(1)

latest_table = tables[-1]
rows = latest_table.find_all("tr")[1:]
print(f"📄 Nombre de lignes dans le dernier tableau : {len(rows)}")

if len(rows) < 3:
    print("⚠️ Pas assez de lignes pour extraire les 3 dernières courses.")
    exit(1)

last_three = []
for i, row in enumerate(rows[-3:], start=1):
    cells = row.find_all("td")
    cell_texts = [cell.text.strip() for cell in cells]
    print(f"🔹 Ligne {i} : {cell_texts}")

    if len(cells) >= 5:
        last_three.append({
            "date": cells[0].text.strip(),
            "type": cells[1].text.strip(),
            "car": cells[2].text.strip(),
            "track": cells[3].text.strip(),
            "notes": cells[4].text.strip()
        })
    else:
        print(f"⚠️ Ligne {i} ignorée : pas assez de colonnes ({len(cells)})")

# Ajouter un timestamp
data = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "races": last_three
}

# Écrire dans le fichier JSON
with open("Daily-Races-1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Fichier Daily-Races-1.json mis à jour avec {len(last_three)} course(s).")
