from typing import List, Dict, Any
import datetime

# Beispielhafte Eingabe für first_experiment_id 
first_experiment_id_input: Any = "100"

try:
    first_experiment_id: int = int(first_experiment_id_input)
except (ValueError, TypeError):
    first_experiment_id = 0

experiments: List[Dict[str, Any]] = []
today_date: str = datetime.date.today().isoformat()

# Erstellen von 10 Leistungstests (Experimenten)
for i in range(10):
    experiment = {
        "id": first_experiment_id + i,
        "date": today_date
    }
    experiments.append(experiment)

# Anzeige der ersten 5 Experimente
for exp in experiments[:5]:
    print(exp)

# Ausgabe, wie viele Experimente mit einer geraden ID erstellt wurden
even_count: int = sum(exp["id"] % 2 for exp in experiments)
print("Anzahl der Experimente mit einer geraden ID:", even_count)

