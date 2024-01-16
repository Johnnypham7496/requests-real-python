import requests


response = requests.get('http://api.github.com', timeout=60)
print(response.content)
print()

# encoding is optional
response.encoding = 'utf-8'
print(response.text)

print()
print(response.json())

# headers provide more information such as the content type and a time limit on how long to cache the response
print()
print(response.headers)
print()
print(response.headers['Content-Type'])
