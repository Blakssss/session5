print('hello, world')

import requests
from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'myproject'}



response = requests.get('https://www.w3schools.com/python/python_sets.asp')
print(response.text)
