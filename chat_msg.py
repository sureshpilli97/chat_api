from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/receive_data/*": {"origins": "*"}})
data = []

@app.route('/receive_data', methods=['POST', 'GET'])
def receive_data():
    global data
    try:
        if request.method == 'POST':
            msg = request.get_json()
            data.append(msg)
            return jsonify({"status": "Message received"})
        elif request.method == 'GET':
            if data and data[0][0]!=request.referrer:
                send = data.pop(0)
                return jsonify(send[1])
            else:
                return jsonify("")
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
