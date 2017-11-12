from api.libraries.execute_python import runCode, generateUUID
from api import APP_PATH
import json

def getMessages():
    messages = []
    with open(APP_PATH + '/data/messages.json') as json_file:
        data = json.load(json_file)
        json_file.close()
        for item in data:
            messages.append(item)
    return messages

def getMessageById(messageId):
    messages = getMessages()
    for message in messages:
        if(message['id'] == messageId):
            return message
    return False

def createMessage(message):
    messages = getMessages()
    messages.append(message)

    with open(APP_PATH + '/data/messages.json', 'w') as outfile:
        json.dump(messages, outfile)
        outfile.close()

    return message

def updateMessage(messageId, data):
    messages=getMessages()
    outputMessage={}
    for message in messages:
        if(message['id'] == messageId):
            for key in data:
                message[key] = data[key]
            outputMessage=message

    with open(APP_PATH + '/data/messages.json', 'w') as outfile:
        json.dump(messages, outfile)
        outfile.close()

    return outputMessage
