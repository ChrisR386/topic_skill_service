from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Topic & Skill Service!"

@app.route('/topics', methods=['GET'])
def get_topics():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'topics.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as file:
            topics = json.load(file)
        return jsonify(topics)
    except FileNotFoundError:
        return jsonify({"error": "Topics data not found."}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON data."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
