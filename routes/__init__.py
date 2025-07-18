from flask import Blueprint, request, jsonify
from data_manager import JsonDataManager

topics_bp = Blueprint('topics_bp', __name__)
topic_data_manager = JsonDataManager('data/topics.json')

@topics_bp.route('/topics/<int:id>', methods=['PUT'])
def update_topic(id):
    data = request.get_json()
    topics = topic_data_manager.load_data()

    # Einfacher Update-Mechanismus: topic mit id suchen
    topic = next((t for t in topics if t['id'] == id), None)
    if not topic:
        return jsonify({'error': 'Topic not found'}), 404

    # Update topic mit den neuen Daten aus JSON
    topic.update(data)
    topic_data_manager.write_data(topics)

    return jsonify(topic), 200
