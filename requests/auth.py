import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth


response = requests.get('https://api.github.com/user', auth=('username', getpass()))
print(response)


requests.get(
     'https://api.github.com/user',
     auth=HTTPBasicAuth('username', getpass())
)