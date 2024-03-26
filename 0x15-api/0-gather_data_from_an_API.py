#!/usr/bin/python3
""" Gather data from an API """


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
        name = user.get('name')
        request = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user_id)
        )
        if request.status_code != 200:
            print('An error has occurred')
            exit(0)
        todos = request.json()
        completed_tasks = []
        for task in todos:
            if task.get('completed') is True:
                completed_tasks.append(task)
        print('Employee {} is done with tasks({}/{}):'.format(
            name, len(completed_tasks), len(todos)))
        for task in completed_tasks:
            print('\t {}'.format(task.get('title')))
