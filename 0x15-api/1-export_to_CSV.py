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
    todo = TODO.json()
    csv_items = []

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
        if 'userId' in item:
            temp_items = []
            temp_items.append(todo.get('userId'))
            temp_items.append(emp_name)
            temp_items.append(todo.get('completed'))
            temp_items.append(todo.get('title'))
            csv_items.append(temp_items)

    with open(f'{emp_id}.csv', 'w+', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_items)
