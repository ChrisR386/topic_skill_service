from flask import Flask, jsonify, request
from data_manager import JsonDataManager

app = Flask(__name__)

# Data Manager für skills.json
skill_data_manager = JsonDataManager('data/skills.json')

@app.route('/skills', methods=['GET'])
def get_skills():
    skills = skill_data_manager.load_data()
    return jsonify(skills)

@app.route('/skills', methods=['POST'])
def create_skill():
    data = request.get_json()
    new_skill = {
        'name': data['name'],
        'topicId': data['topicId'],
        'difficulty': data.get('difficulty', 'beginner')
    }

    # Daten laden, neuen Skill hinzufügen, speichern
    skills = skill_data_manager.load_data()
    skills.append(new_skill)
    skill_data_manager.write_data(skills)

    return jsonify(new_skill), 201

if __name__ == '__main__':
    app.run(debug=True)
