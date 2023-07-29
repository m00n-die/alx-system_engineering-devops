#!/usr/bin/python3
"""Module that gets data from an api"""
import csv
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
    user_name = str(user.json().get("username"))
    todo = TODO.json()
    dictionary = {}
    file_name = 'todo_all_employees.json'

    for elem in user:
        todos = []
        for todo in todos:
            if todo.get("userId") == user.get("id"):
                my_dict = {"username": user.get("username"),
                           "task": todo.get("title"),
                           "completed": todo.get("completed")}
                todos.append(my_dict)
       
        dictionary[user.get("id")] = todos
    with open(file_name, 'w+') as f:
        json.dump(dictionary, f)
