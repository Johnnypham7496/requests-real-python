# timeouts are for preventing traffic being backedup. If a timeout is present it will try to reach out to the server. 
# if call to the external service has not been retrieved before timeout ends, the request will stop and the end user will have to retry
import requests


one_second_timeout= requests.get('https://api.github.com', timeout=1)
print(one_second_timeout)

three_second_timeout= requests.get('https://api.github.com', timeout=3.05)
print(three_second_timeout)