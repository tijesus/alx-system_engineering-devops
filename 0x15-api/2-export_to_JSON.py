#!/usr/bin/python3
""" Exporting the employee data to csv"""

import requests as r
import sys
import json

if __name__ == "__main__":
    user_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + user_id

    response = r.get(url)
    username = response.json().get('username')
    todoUrl = url + "/todos"
    response = r.get(todoUrl)
    user_todo = response.json()

    dict = {user_id: []}
    for todo in user_todo:
        dict[user_id].append({
            "task": todo.get("title"),
            "completed": todo.get('completed'),
            "username": username
        })

    with open('{}.json'.format(user_id), 'w') as filename:
        json.dump(dict, filename)
