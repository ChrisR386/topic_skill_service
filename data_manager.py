import json
import os

class JsonDataManager:
    def __init__(self, filename):
        self.filename = filename
        # Stelle sicher, dass die Datei existiert
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f)  # Leere Liste als Anfang

    def load_data(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def write_data(self, data):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)