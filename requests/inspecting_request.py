# a way for inspecting what the payload of the request is before being sent
import requests


response = requests.post('https://httpbin.org/post', json={'key':'value'}, timeout=60)
response.request.headers['Content-Type']

print(response.request.url)

print(response.request.body)
