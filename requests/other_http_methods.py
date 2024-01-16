import requests


requests.post('https://httpbin.org/post', data={'key':'value'}, timeout=60)
requests.put('https://httpbin.org/put', data={'key':'value'}, timeout=60)
requests.delete('https://httpbin.org/delete', timeout=60)
requests.head('https://httpbin.org/get', timeout=60)
requests.patch('https://httpbin.org/patch', data={'key':'value'}, timeout=60)
requests.options('https://httpbin.org/get', timeout=60)


response = requests.head('https://httpbin.org/get', timeout=60)
response.headers['Content-Type']
print(response)

response = requests.delete('https://httpbin.org/delete', timeout=60)
json_response = response.json()
print(json_response['args'])
