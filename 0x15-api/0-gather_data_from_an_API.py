#!/usr/bin/python3
'''
gather employee data from API
'''

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos"\
        .format(user_id)
    response = requests.get(url).json()
    username = response.get('name')
    done_todos = 0
    user_todos = requests.get(user_todos_url).json()
    total_todos = len(user_todos)
    for todo in user_todos:
        if todo.get("completed"):
            done_todos += 1
    print("Employee {} is done with tasks ({}/{}):"
          .format(username, done_todos, total_todos))

    for todos in user_todos:
        if todos.get("completed"):
            print("\t {}".format(todos.get("title")))
