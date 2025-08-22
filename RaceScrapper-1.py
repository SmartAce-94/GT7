import requests
from bs4 import BeautifulSoup
import json

url = "https://gran-turismo.fandom.com/wiki/Sport_Mode_(GT7)/Daily_Races"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", {"class": "wikitable"})
latest_table = tables[-1]
rows = latest_table.find_all("tr")[1:]

# Extraire les 3 dernières courses
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

# Sauvegarder dans un fichier JSON
with open("courses.json", "w", encoding="utf-8") as f:
    json.dump(last_three, f, ensure_ascii=False, indent=2)
