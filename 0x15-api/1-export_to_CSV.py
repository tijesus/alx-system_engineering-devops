#!/usr/bin/python3
""" Exporting the employee data to csv"""

import requests as r
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + user_id

    response = r.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = r.get(todoUrl)
    user_todo = response.json()

    with open('{}.csv'.format(user_id), 'w') as file:
        for todo in user_todo:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, username, todo.get('completed'),
                               todo.get('title')))
