import requests


response = requests.get('https://api.github.com', verify=True)
print(response)
