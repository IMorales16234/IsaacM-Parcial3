from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id":1, "nombre":"isaac", "enable":True},
    {"id":2, "nombre":"naye", "enable":False},
    {"id":3, "nombre":"jessie", "enable":True},
    {"id":4, "nombre":"corpi", "enable":False},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)