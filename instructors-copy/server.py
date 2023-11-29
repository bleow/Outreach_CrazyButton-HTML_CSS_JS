# IMPORT // libraries that will help us with creating the backend server
import os
from random import uniform
from aiohttp import web
import socketio


# INITIALISATION // create a web app, web socket, and bind the web app to the web socket
sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


async def index(request):
    """
    (coroutine) Request handler to serve our webpage
    :param request: Request instance
    :return: StreamResponse-derived (e.g. Response) instance
    """
    CUR_DIRECTORY = os.getcwd()
    INDEX_DIRECTORY = CUR_DIRECTORY + '\\index.html'
    with open(INDEX_DIRECTORY) as f:
        return web.Response(text=f.read(), content_type='text/html')


## We bind our aiohttp endpoint to our app
## router
app.router.add_get('/', index)

# keep track of list of connected players
# {  player1_sid: score,
#    player2_sid: score,
#    player3_sid: score,
#    ...
# }
playerList = {}


# start of event handlers
# a player has joined
@sio.event
async def connect(sid, _):
    # print when new player has connected
    print('new player : ', sid)

    # add player to playerList with initial score of 0
    playerList[sid] = 0

    # announce to everybody connected that a new player has connected
    # with payload of playerList
    await sio.emit('player_connected', {'playerList': playerList})


# a player has left
@sio.event
async def disconnect(sid):
    # remove player from playerList
    playerList.pop(sid)

    # announce to everybody connected that a player has disconnected
    # with payload of playerList
    await sio.emit('player_disconnected', {'playerList': playerList})


# a player has pressed the button
@sio.event
async def button_pressed(sid):
    # randomTop and randonLeft is value between [0, 1]
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


# end of event handlers

# start server
if __name__ == '__main__':
    web.run_app(app)
