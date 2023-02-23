#!/usr/bin/python3
"""A script using  REST API for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


"""Import Libs"""

if __name__ == "__main__":
    user_id = int(sys.argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    todo_data = requests.get(todos_url).json()

    employee_name = requests.get(users_url).json()["name"]

    total_user_todos = 0
    completed_todos = 0
    titles = []
    for todo in todo_data:
        if user_id == todo["userId"]:
            total_user_todos += 1
            if todo["completed"]:
                completed_todos += 1
                titles.append(todo["title"])

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_todos, total_user_todos))

    for title in titles:
        print("\t {}".format(title))
