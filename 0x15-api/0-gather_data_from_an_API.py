#!/usr/bin/python3
"""Module that gets data from an api"""
import json
import requests
import sys


if __name__ == "__main__":
    """starts the script"""
    all_tasks = 0
    completed_tasks = 0
    emp_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{emp_id}")
    TODO = requests.get(f"{url}/todos", params={"userId": emp_id})
    emp_name = str(user.json().get("name"))
    todo = TODO.json()

    """
    for item in todo:
        if 'userId' in item:
            all_tasks += 1
        if 'completed' in item:
            completed_tasks += 1
    """

    complete = []
    for item in todo:
        if item.get('completed') is True:
            complete.append(item.get('title'))

    print("Employee {} is done with tasks({}/{}):".format
          (emp_name, len(complete), len(todo)))
    """
    print("Employee {} is done with tasks({}/{}):".format
          (emp_name, completed_tasks, all_tasks))
    """

    [print("\t {}".format(elem)) for elem in complete]
