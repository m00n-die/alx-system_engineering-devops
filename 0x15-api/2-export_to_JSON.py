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
    csv_items = []

    with open(f'{emp_id}.json', 'w+') as file:
        json.dump({emp_id: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_name} for item in todo]}, file)
