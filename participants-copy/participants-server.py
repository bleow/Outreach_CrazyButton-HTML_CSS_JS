"""
Stage 3
Purpose: 
- Set up the basic operations on the backend
Key points:
- Initialise server basics
- Routing
"""

"""
Stage 4 - Server
Purpose: 
- Set up sockets, socket logic, and logging
Key points:
- Websockets
    - Listen to and emit signals
- Logic
- Logging
- Type alias/hinting
"""

"""
Stage 5 - Server
Purpose: 
- Clean up and fix button initial location bug
Key points:
- Sending signals to specific users
"""

# IMPORT // libraries that will help us with creating the backend server
import os
from aiohttp import web


# INITIALISATION // create a web app
# https://docs.python.org/3/howto/logging-cookbook.html
# TODO stage 4: logger

# https://python-socketio.readthedocs.io/en/latest/api.html#socketio.AsyncServer
# TODO stage 4: bind logger to socket

# https://python-socketio.readthedocs.io/en/latest/server.html#aiohttp
# TODO stage 3: make web app

# https://docs.python.org/3/howto/logging-cookbook.html
# TODO stage 4: configure logger

# https://docs.python.org/3/library/typing.html#type-aliases
# TODO stage 4: make type alias for PlayerList

def index(request):
    """
    Request handler to serve our webpage
    :param request: Request instance
    :return: StreamResponse-derived (e.g. Response) instance
    """
    DIRECTORY = ""  # TODO stage 3: get directory of index.html
    with open(DIRECTORY) as f:
        return web.Response(text=f.read(), content_type='text/html')


#TODO stage 4: debug this connect() code
@sio.on('connect')
async def connect(sid):
    """
    A player has joined the server.
    https://python-socketio.readthedocs.io/en/latest/api.html#socketio.Server.on
    :param sid: ID of player that joined
    :param _: Web Server Gateway Interface (WSGI) environment https://www.fullstackpython.com/wsgi-servers.html
    :return: False to reject the connection or null
    """
    sio.logger.info(f'New player joined: {sid}')

    # add player to playerList with initial score of 0
    playerList[sid] = 0

    # announce to everybody connected that a new player has connected
    # with payload of playerList
    await sio.emit('player_connected', {'playerList': playerList})


async def disconnect():
    """
    A player has left the server.
    https://python-socketio.readthedocs.io/en/latest/api.html#socketio.Server.on
    :param sid: ID of player that left
    :return:
    """
    # TODO stage 4: write the disconnect() code

async def button_pressed():
    # TODO stage 4: write the button_pressed code

# ROUTING // bind our aiohttp endpoint to our app router
app.router.add_get('/', index)

# start server
# TODO stage 3: write code to start the server
