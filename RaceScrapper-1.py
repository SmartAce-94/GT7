import requests
from bs4 import BeautifulSoup

url = "https://gran-turismo.fandom.com/wiki/Sport_Mode_(GT7)/Daily_Races"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Trouver tous les tableaux de courses
tables = soup.find_all("table", {"class": "wikitable"})

# On suppose que le dernier tableau est le plus récent
latest_table = tables[-1]
rows = latest_table.find_all("tr")[1:]  # Ignorer l'en-tête

# Extraire uniquement les 3 dernières lignes
for row in rows[-3:]:
    cells = row.find_all("td")
    if len(cells) >= 5:
        date = cells[0].text.strip()
        course_type = cells[1].text.strip()
        car = cells[2].text.strip()
        track = cells[3].text.strip()
        notes = cells[4].text.strip()
        print(f"{date} | {course_type} | {car} | {track} | {notes}")
