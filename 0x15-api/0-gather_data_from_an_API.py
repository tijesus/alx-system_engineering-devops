#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + user_id

    response = requests.get(url)
    username = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    user_todos = response.json()
    done = 0
    done_tasks = []

    for todo in user_todos:
        if todo.get('completed'):
            done_tasks.append(todo)
            done += 1

    print("Employee {} is done with user_todos({}/{}):"
          .format(username, done, len(user_todos)))

    for todo in done_tasks:
        print("\t {}".format(todo.get('title')))