#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API."""
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    user = requests.get("{}/users/{}".format(BASE_URL, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(BASE_URL), params={"userId": employee_id}
    ).json()

    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todos)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
