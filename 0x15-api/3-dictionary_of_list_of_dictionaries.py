#!/usr/bin/python3
""" Gather data from an API
addition to the first task, export all task data in the json format.
FORMAT:
{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS},
{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}
    > output File name is todo_all_employees.json
"""


import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    request = requests.get(url)
    if request.status_code != 200:
        print('An error has occurred')
        exit(0)
    else:
        response = request.json()

    dict_all = {}
    for user in response:
        user_id = user.get('id')
        username = user.get('username')
        request = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user_id)
        )
        if request.status_code != 200:
            print('An error has occurred')
            exit(0)
        todos = request.json()

        todo_dict = json.dumps(
            {user_id: [
                {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                for task in todos
            ]}
            )
        dict_all.update(json.loads(todo_dict))
    with open(f'todo_all_employees.json', 'w') as file:
        json.dump(dict_all, file)
