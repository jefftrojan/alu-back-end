#!/usr/bin/python3
""" returns TODO list """


import requests
import sys

employee_id = sys.argv[1]
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

if response.status_code != 200:
    print(f"Error retrieving TODO list for employee ID {employee_id}")
    sys.exit(1)

todos = response.json()
completed_tasks = [todo for todo in todos if todo["completed"]]
total_tasks = len(todos)

employee_name = todos[0]["username"]
print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")

for todo in completed_tasks:
    print(f"\t{todo['title']}")

