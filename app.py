from flask import Flask, jsonify, request
from data_manager import JsonDataManager
from routes.topics import topics_bp  # Importiere Blueprint

app = Flask(__name__)

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
    skills = skill_data_manager.load_data()
    skills.append(new_skill)
    skill_data_manager.write_data(skills)
    return jsonify(new_skill), 201

# Blueprint registrieren
app.register_blueprint(topics_bp)

if __name__ == '__main__':
    app.run(debug=True)