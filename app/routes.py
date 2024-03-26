from flask import request
from . import app
from hw_data.tasks import tasks_list

@app.route('/tasks')
def get_tasks():
    # Get the posts from storage (fake data -> tomorrow will be db)
    tasks = tasks_list
    return tasks

@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    # Get the posts from storage
    tasks = tasks_list
    # For each dictionary in the list of post dictionaries
    for task in tasks:
        # If the key of 'id' matches the post_id from the URL
        if task['id'] == task_id:
            # Return that post dictionary
            return task
    # If we loop through all of the posts without returning, the post with that ID does not exist
    return {'error': f"Post with an ID of {task_id} does not exist"}, 404