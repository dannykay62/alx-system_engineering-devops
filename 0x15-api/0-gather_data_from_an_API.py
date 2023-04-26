#!/usr/bin/python3
"""returns information about TODO list progress of a given employee ID"""
import sys
import requests

if __name__ == "__main__":
	url = "jsonplaceholder.typicode.com/"
	user = requests.get(url + "users/{}".format(sys.argv[1])).json()
	todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

	completed = [tit.get("title") for tit in todos if tit.get("completed") is True]
	print("Employee {} is done with tasks({}/{}):".format( user.get("name"),
		 len(completed), len(todos)))
	[print("\t {}".format(cp)) for cp in completed]
