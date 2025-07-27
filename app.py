from flask import Flask, jsonify, request, abort

# Initialize the Flask application
app = Flask(__name__)

# Simulated in-memory database: a list of tasks
tasks = [
    {
        'id': 1,
        'title': 'Learn Flask',
        'description': 'Build a REST API using Flask',
        'done': False
    },
    {
        'id': 2,
        'title': 'Submit assignment',
        'description': 'Submit Lab 4',
        'done': False
    }
]

# Helper function to format API responses consistently
def make_response(success=True, message="", data=None):
    return jsonify({
        'success': success,
        'message': message,
        'data': data
    })

# GET /tasks - Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return make_response(data=tasks)

# GET /tasks/<task_id> - Retrieve a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return make_response(False, f'Task {task_id} not found'), 404
    return make_response(data=task)

# POST /tasks - Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    # Check if the request is valid and contains 'title'
    if not request.json or 'title' not in request.json:
        return make_response(False, 'Invalid input'), 400
    # Create a new task using the request data
    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(new_task)
    return make_response(True, 'Task created', new_task), 201

# PUT /tasks/<task_id> - Update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return make_response(False, 'Task not found'), 404
    if not request.json:
        return make_response(False, 'Invalid request'), 400
    # Update task fields with new values if provided
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return make_response(True, 'Task updated', task)

# DELETE /tasks/<task_id> - Delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return make_response(False, 'Task not found'), 404
    # Remove the task from the list
    tasks = [t for t in tasks if t['id'] != task_id]
    return make_response(True, f'Task {task_id} deleted')

# Entry point: start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
