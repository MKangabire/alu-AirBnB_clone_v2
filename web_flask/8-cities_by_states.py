#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, jsonify
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', methods=['GET'])
def cities_by_states():
    """Returns a JSON list of all State objects"""
    states = storage.all("State").values()
    if not states:
        return 'No states found', 500
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)