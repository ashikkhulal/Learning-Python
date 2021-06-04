# an example of getting a api requests


import requests

response = requests.get("https://api.github.com/users/ashikkhulal/repos")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['url']}\n")