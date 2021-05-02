#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from calendar import timegm
from datetime import datetime
import _strptime  # https://bugs.python.org/issue7980
from flask import Flask, request, jsonify
from powerdb_reader import PowerDbReader

app = Flask(__name__)
app.debug = True

powerDbReader = None

def convert_to_time_ms(timestamp):
    return 1000 * timegm(datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())

@app.route("/")
def health_check():
    return "ok"

@app.route('/search', methods=['POST'])
def search():
    series = powerDbReader.get_plug_names()
    return jsonify(series)

@app.route('/query', methods=['POST'])
def query():
    req = request.get_json()

    from_ = convert_to_time_ms(req['range']['from'])
    to = convert_to_time_ms(req['range']['to'])

    data = []
    for target in req['targets']:
        target_name = target['target']
        target_id = powerDbReader.plug_name_to_id(target_name)
        data.append(
            {
                "target": target['target'],
                "datapoints": powerDbReader.get_data_in_range(target_id, from_, to)
            })

    return jsonify(data)

@app.route('/annotations', methods=['POST'])
def annotations():
    req = request.get_json()
    print(req)
    data = [
        {
            "annotation": 'This is the annotation',
            "time": (convert_to_time_ms(req['range']['from']) +
                     convert_to_time_ms(req['range']['to'])) / 2,
            "title": 'Deployment notes',
            "tags": ['tag1', 'tag2'],
            "text": 'Hm, something went wrong...'
        }
    ]
    return jsonify(data)

@app.after_request
def after_request(response):
    # CORS headers
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

if __name__ == "__main__":
    #TODO get powerdb file path as param
    powerDbReader = PowerDbReader("/home/anurag/Sync/db/powerdb")
    app.run()
