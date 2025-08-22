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
tables = soup.find_all("table", {"class": "wikitable"})

if not tables:
    print("⚠️ Aucun tableau trouvé. Le format de la page a peut-être changé.")
    exit(1)

latest_table = tables[-1]
rows = latest_table.find_all("tr")[1:]

if len(rows) < 3:
    print("⚠️ Pas assez de lignes pour extraire les 3 dernières courses.")
    exit(1)

last_three = []
for row in rows[-3:]:
    cells = row.find_all("td")
    if len(cells) >= 5:
        last_three.append({
            "date": cells[0].text.strip(),
            "type": cells[1].text.strip(),
            "car": cells[2].text.strip(),
            "track": cells[3].text.strip(),
            "notes": cells[4].text.strip()
        })

# Ajouter un timestamp
data = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "races": last_three
}

# Écrire dans le fichier JSON
with open("Daily-Races-1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Fichier Daily-Races-1.json mis à jour avec les dernières courses.")
