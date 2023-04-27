#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": tit.get("title"),
                "completed": tit.get("completed"),
                "username": u.get("username")
            } for tit in requests.get(url + "todos",
                                      params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
