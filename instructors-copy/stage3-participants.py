"""
Stage 3
Purpose: 
- Set up the basic operations on the backend
Key points:
- Initialise server basics
- Routing
"""

# IMPORT // libraries that will help us with creating the backend server
import os
from aiohttp import web


# INITIALISATION // create a web app
# https://python-socketio.readthedocs.io/en/latest/server.html#aiohttp
# TODO stage 3: make web app

def index(request):
    """
    Request handler to serve our webpage
    :param request: Request instance
    :return: StreamResponse-derived (e.g. Response) instance
    """
    DIRECTORY = "" # TODO stage 3: get directory of index.html
    with open(DIRECTORY) as f:
        return web.Response(text=f.read(), content_type='text/html')


# ROUTING // bind our aiohttp endpoint to our app router
app.router.add_get('/', index)

# start server
# TODO stage 3: write code to start the server
