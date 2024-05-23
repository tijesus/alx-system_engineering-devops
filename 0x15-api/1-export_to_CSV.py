#!/usr/bin/python3
""" Exporting the employee data to csv"""

import requests as r
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_todos_url = url + "/" "todos"
    response = r.get(url).json()
    username = response.get("name")
    user_todos = r.get(user_todos_url).json()
    with open('{}.csv'.format(user_id), 'w') as file:
        for todo in user_todos:
            done_task_status = todo.get("completed")
            task_title = todo.get("title")
            file.write('"{}","{}","{}","{}"\n'
                  .format(user_id, username, done_task_status, task_title))
