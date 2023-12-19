# raising exception if the response was unsuccessful
from requests.exceptions import HTTPError
from security import safe_requests


for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = safe_requests.get(url)

        # if the response is successful, No exception is raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error has occurred: {http_err}')
    except Exception as err:
        print(f'Other error has occurred: {err}')
    else:
        print('Success!')
