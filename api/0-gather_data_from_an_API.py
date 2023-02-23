#!/usr/bin/python3
""" returns TODO list """


import urllib.request
import json
import sys

""" Get the employee ID from the command-line argument """
employee_id = sys.argv[1]

""" Construct the API URL with the employee ID as a query parameter """
url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

""" Use urllib to make a GET request to the API endpoint and retrieve the TODO list """
try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
except urllib.error.HTTPError:
    """ Handle errors if the employee ID is not found or there is some other problem with the API """
    print(f"Error retrieving TODO list for employee ID {employee_id}")
    sys.exit(1)

""" Filter the TODO list to get only the completed tasks and count them """
completed_tasks = [todo for todo in data if todo["completed"]]
total_tasks = len(data)

""" Get the name of the employee from the first TODO item in the list """
employee_name = data[0]["username"]

""" Print the TODO list progress in the required format """
print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
for todo in completed_tasks:
    print(f"\t{todo['title']}")
