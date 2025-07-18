from flask import Blueprint, request, jsonify
from data_manager import JsonDataManager

topics_bp = Blueprint('topics', __name__)
topic_data_manager = JsonDataManager('data/topics.json')

@topics_bp.route('/topics', methods=['POST'])
def create_topic():
    data = request.get_json()
    new_topic = {
        'id': data['id'],
        'name': data['name'],
        'description': data['description']
    }

    topics = topic_data_manager.load_data()
    topics.append(new_topic)
    topic_data_manager.write_data(topics)

    return jsonify(new_topic), 201