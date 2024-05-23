#!/usr/bin/python3
""" Exporting the employee data to json"""

import json
import requests as r
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = r.get(url)
    users = response.json()

    dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = r.get(url)
        tasks = response.json()
        dict[user_id] = []
        for todo in tasks:
            dict[user_id].append({
                "username": username,
                "todo": todo.get('title'),
                "completed": todo.get('completed')
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dict, file)
