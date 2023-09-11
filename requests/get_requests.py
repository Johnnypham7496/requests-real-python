import requests


response = requests.get('http://api.github.com/')
print(response)

# prints the status code of the get request
print(response.status_code)