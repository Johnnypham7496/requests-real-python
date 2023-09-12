import requests


requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get')


response = requests.head('https://httpbin.org/get')
response.headers['Content-Type']
print(response)

response = requests.delete('https://httpbin.org/delete')
json_response = response.json()
print(json_response['args'])