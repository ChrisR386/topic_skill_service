# Flask ist das Web-Framework, das wir für unsere API verwenden.
from flask import Flask, jsonify
import json  # Zum Laden der JSON-Datei mit den Topics
import os    # Um Dateipfade systemunabhängig zu verarbeiten

# Wir erstellen eine Flask-App-Instanz.
app = Flask(__name__)

# Basisroute: Testet, ob der Service erreichbar ist.
@app.route('/')
def hello():
    return "Hello from Topic & Skill Service!"

# /topics-Endpunkt: Gibt die Inhalte aus topics.json zurück
@app.route('/topics', methods=['GET'])
def get_topics():
    # Pfad zur Datei topics.json im Unterordner data
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'topics.json')
    try:
        # Öffne und lade die JSON-Daten
        with open(data_path, 'r', encoding='utf-8') as file:
            topics = json.load(file)
        # Gebe die geladenen Daten als JSON-Antwort zurück
        return jsonify(topics)
    except FileNotFoundError:
        # Fehlerfall: Datei nicht gefunden
        return jsonify({"error": "Topics data not found."}), 404
    except json.JSONDecodeError:
        # Fehlerfall: JSON ungültig oder beschädigt
        return jsonify({"error": "Error decoding JSON data."}), 500

# Starte die Flask-App, wenn die Datei direkt ausgeführt wird
if __name__ == '__main__':
    app.run(debug=True, port=5000)