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

# IMPORT // libraries that will help us with creating the backend server
import os
import logging
from random import uniform
from typing_extensions import TypeAlias, Dict

from aiohttp import web
import socketio

### Initialisation -> create a web app, web socket, and bind the web app to the web socket
# https://docs.python.org/3/howto/logging-cookbook.html
logger = logging.getLogger('crazy_button_logger')

# https://python-socketio.readthedocs.io/en/latest/api.html#socketio.AsyncServer
sio = socketio.AsyncServer(logging=logger)

# https://python-socketio.readthedocs.io/en/latest/server.html#aiohttp
app = web.Application()
sio.attach(app)

# https://docs.python.org/3/howto/logging-cookbook.html
sio.logger.setLevel(logging.DEBUG)
format = logging.Formatter('==== CRAZY BUTTON LOGS : %(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Sends logs to file
fh = logging.FileHandler('debug.log')
fh.setFormatter(format)
sio.logger.addHandler(fh)

# Sends logs to console
ch = logging.StreamHandler()
ch.setFormatter(format)
sio.logger.addHandler(ch)

### Global variables and type hinting
# Keep track of list of connected players
# {  player1_sid: score,
#    player2_sid: score,
#    player3_sid: score,
#    ...
# }
# https://docs.python.org/3/library/typing.html#type-aliases
PlayerSid: TypeAlias = str
Score: TypeAlias = int
PlayerList: TypeAlias = Dict[PlayerSid, Score]
playerList: PlayerList = {}


### Logic Functions
# Functional Req: Serve index page, connect, disconnect, click

def index(request):
    """
    Request handler to serve our webpage
    :param request: Request instance
    :return: StreamResponse-derived (e.g. Response) instance
    """
    CUR_DIRECTORY = os.getcwd()
    INDEX_DIRECTORY = CUR_DIRECTORY + '\\stage4.html'
    with open(INDEX_DIRECTORY) as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.on('connect')
async def connect(sid, _):
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


@sio.on('disconnect')
async def disconnect(sid):
    """
    A player has left the server.
    https://python-socketio.readthedocs.io/en/latest/api.html#socketio.Server.on
    :param sid: ID of player that left
    :return:
    """
    # remove player from playerList
    playerList.pop(sid)

    # announce to everybody connected that a player has disconnected
    # with payload of playerList
    await sio.emit('player_disconnected', {'playerList': playerList})


@sio.event  # Simplified version of the sio.on() method that takes the event name from the decorated function
async def button_pressed(sid):
    """
    A player has pressed the button.
    :param sid: ID of player that pressed it
    :return:
    """
    # randomTop and randonLeft is value between [0, 0.95]
    randomTop = uniform(0, 0.95)
    randomLeft = uniform(0, 0.95)

    # increase player score by 1
    playerList[sid] += 1

    # announce to everybody connected that a player has pressed the button
    # with payload of randomTop, randomLeft to move button on all players screen
    # and playerList to update the score on the player screen
    await sio.emit(
        'new_button_location', {
            'randomTop': randomTop,
            'randomLeft': randomLeft,
            'playerList': playerList,
        })


# ROUTING // bind our aiohttp endpoint to our app router
app.router.add_get('/', index)

# start server
if __name__ == '__main__':
    web.run_app(app, port=8080)
