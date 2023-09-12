import requests


response = requests.get('https://api.github.com', verify=False)
print(response)