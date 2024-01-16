import requests


response = requests.get('https://api.github.com', verify=False, timeout=60)
print(response)
