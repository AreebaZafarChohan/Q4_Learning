users = {}
tasks = {}

user_id_counter = 1
task_id_counter = 1

def create_user(user):
    global user_id_counter
    user_dict = user.dict()
    user_dict["id"] = user_id_counter
    users[user_id_counter] = user_dict
    user_id_counter += 1
    return user_dict

def get_user(user_id):
    return users.get(user_id)

def delete_user(user_id):
    return users.pop(user_id, None)

def create_task(task):
    global task_id_counter
    task_dict = task.dict()
    task_dict["id"] = task_id_counter
    tasks[task_id_counter] = task_dict
    task_id_counter += 1
    return task_dict

def get_task(task_id):
    return tasks.get(task_id)

def update_task(task_id, task_update):
    task = tasks.get(task_id)
    if task:
        tasks["status"] = task_update.status
    return task

def delete_task(task_id):
    return tasks.pop(task_id, None) 

def get_tasks_by_user(user_id):
    return [t for t in tasks.values() if t["user_id"] == user_id ]
   