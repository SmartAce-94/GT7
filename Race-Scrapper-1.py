import json
from datetime import datetime

# Générer un timestamp
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Créer un dictionnaire simple
data = {
    "last_updated": now
}

# Écrire dans le fichier JSON
with open("Daily-Races-1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Fichier Daily-Races-1.json mis à jour avec le timestamp.")
