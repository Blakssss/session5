print('hello, world')

import requests

response = requests.get('https://www.w3schools.com/python/python_sets.asp')
print(response.text)
