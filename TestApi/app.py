from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Task 1", "description": "Example task 1", "done": True},
    {"id": 2, "title": "Task 1", "description": "Example task 1", "done": False}
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/tasks", methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})


@app.route("/api/tasks", methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks)+1,
        "title": data['title'],
        "description": data['description'],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


if __name__ == "__main__":
    app.run(debug=True)