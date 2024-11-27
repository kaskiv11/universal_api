from flask import Flask, jsonify, request, render_template, abort
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler('app.log'),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger(__name__)

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
    logger.info(f"New task added with ID {new_task['id']}")
    return jsonify(new_task), 201


@app.route("/api/tasks/<int:task_id>", methods=['DELETE'])
def delete_task(task_id):
    logger.info("Deleting task appi(api/tasks/<int:task_id>) me  methods=['DELETE']")
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        logger.warning(f"Task with ID {task_id} not found")
        abort(404, message="Task not found")
    tasks.remove(task)
    logger.info(f"Deleted task with ID {task_id}")
    return jsonify({"message": f"Task {task_id} deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)