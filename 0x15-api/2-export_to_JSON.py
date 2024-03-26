#!/usr/bin/python3
""" Gather data from an API
addition to the first task, export data in the json format.
({ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, ... ]})
    > output File name is USER_ID.json
"""


import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} user_id'.format(sys.argv[0]))
        exit(0)
    if not sys.argv[1].isdigit():
        print('User id must be an integer')
        exit(0)
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    request = requests.get(url)
    if request.status_code != 200:
        print('An error has occurred')
        exit(0)
    else:
        response = request.json()

    for user in response:
        user_id = user.get('id')
        if user_id != int(id):
            continue
        username = user.get('username')
        request = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user_id)
        )
        if request.status_code != 200:
            print('An error has occurred')
            exit(0)
        todos = request.json()
        with open(f'{user_id}.json', 'w') as file:
            writer = json.dump(
                {user_id: [
                    {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": username}
                    for task in todos
                ]},
                file
            )
