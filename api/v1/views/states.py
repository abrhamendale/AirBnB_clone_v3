#!/usr/bin/python3
@app_view.route('/api/v1/states', methods=['GET'])
def get_all():
    """Queries all elemets."""
    q = session.query(states)

@app_view.route('/api/v1/states/<state_id>', methods=['GET'])
@app_view.route('/api/v1/states/<state_id>', methods=['DELETE'])
@app_view.route('/api/v1/states', methods=['POST'])
@app_view.route('/api/v1/states/<state_id>', methods=['PUT'])

