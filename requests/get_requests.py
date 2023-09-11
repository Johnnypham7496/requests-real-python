import requests


response = requests.get('http://api.github.com/')
print(response)

# prints the status code of the get request
print(response.status_code)


# if statement 
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not found')