from api.libraries.execute_python import runCode, generateUUID
from api import APP_PATH
import json

def getRooms():
    rooms = []
    with open(APP_PATH + '/data/rooms.json') as json_file:
        data = json.load(json_file)
        json_file.close()
        for item in data:
            rooms.append(item)
    return rooms

def getRoomById(roomId):
    rooms = getRooms()
    for room in rooms:
        if(room['id'] == roomId):
            return room
    return False

def createRoom(consumer, dfCode):
    room = {}
    dfState = runCode(dfCode, {})
    room = {
        "id": generateUUID(),
        "dfState": dfState['df'],
        "dataStore": None,
        "consumer": consumer
    }
    rooms = getRooms()
    rooms.append(room)

    with open(APP_PATH + '/data/rooms.json', 'w') as outfile:
        json.dump(rooms, outfile)
        outfile.close()

    return room

def updateRoom(roomId, data):
    rooms=getRooms()
    outputRoom = {}
    for room in rooms:
        if(room['id'] == roomId):
            for key in data:
                room[key] = data[key]
            outputRoom=room

    with open(APP_PATH + '/data/rooms.json', 'w') as outfile:
        json.dump(rooms, outfile)
        outfile.close()

    return outputRoom
