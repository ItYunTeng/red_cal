from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return "API is running!"


@app.route('/data', methods=['GET'])
def data():
    response_data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
