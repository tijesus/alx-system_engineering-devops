#!/usr/bin/python3
"""Using this REST API, for a received employee ID,
displaying the title of completed user_todos."""

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + user_id

    response = requests.get(url)
    username = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    user_todos = response.json()
    done = 0

    for todo in user_todos:
        if todo.get('completed'):
            done += 1

    print("Employee {} is done with user_todos({}/{}):"
          .format(username, done, len(user_todos)))

    for todo in user_todos:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))
