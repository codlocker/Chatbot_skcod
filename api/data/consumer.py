from api.libraries.execute_python import runCode, generateUUID
from api import APP_PATH
import json

def getConsumers():
    consumers = []
    with open(APP_PATH + '/data/consumers.json') as json_file:
        data = json.load(json_file)
        json_file.close()
        for item in data:
            consumers.append(item)
    return consumers

def getConsumerById(consumerId):
    consumers = getConsumers()
    for consumer in consumers:
        if(consumer['id'] == consumerId):
            return consumer
    return False

def getConsumerByPhone(phone, consumers):
    consumerPhone = {}
    for consumer in consumers:
        if('phone' in consumer and consumer['phone'] == phone):
            consumerPhone = consumer
    if('phone' in consumerPhone and consumerPhone['phone'] != None):
        return consumerPhone
    else:
        return False

def getConsumerByEmail(email, consumers):
    consumerEmail = {}
    for consumer in consumers:
        if('email' in consumer and consumer['email'] == email):
            consumerEmail = consumer
    if('email' in consumerEmail and consumerEmail['email'] != None):
        return consumerEmail
    else:
        return False

def getConsumerByFacebookId(facebookId, consumers):
    consumerFacebookId = {}
    for consumer in consumers:
        if('facebookId' in consumer and consumer['facebookId'] == facebookId):
            consumerFacebookId = consumer
    if('facebookId' in consumerFacebookId and consumerFacebookId['facebookId'] != None):
        return consumerFacebookId
    else:
        return False

def updateConsumerById(consumerId, data):
    consumers=getConsumers()
    outputConsumer = {}
    for consumer in consumers:
        if(consumer['id'] == consumerId):
            for key in data:
                consumer[key] = data[key]
            outputConsumer=consumer

    with open(APP_PATH + '/data/consumers.json', 'w') as outfile:
        json.dump(consumers, outfile)
        outfile.close()

    return outputConsumer

def createConsumer(body):
    consumers = getConsumers()
    email      =body.get("email", "")
    name       =body.get("name", "")
    facebookId =body.get("facebookId","")
    phone      =body.get("phone", "")

    consumerPhone = {}
    consumerEmail = {}
    consumerFacebookId = {}

    if(phone != ""):
        consumerPhone = getConsumerByPhone(phone, consumers)

    if(facebookId != ""):
        consumerFacebookId = getConsumerByFacebookId(facebookId, consumers)

    if(email != ""):
        consumerEmail = getConsumerByEmail(email, consumers)

    if(consumerPhone):
        consumerPhone['email'] = email if email != "" else consumerPhone['email']
        consumerPhone['facebookId'] = facebookId if facebookId != "" else consumerPhone['facebookId']
        consumerPhone['name'] = name if name != "" else consumerPhone['name']
        consumer=updateConsumerById(consumerPhone['id'], consumerPhone)
        return consumer
    elif(consumerFacebookId):
        consumerFacebookId['email'] = email if email != "" else consumerFacebookId['email']
        consumerFacebookId['phone'] = phone if phone != "" else consumerFacebookId['phone']
        consumerFacebookId['name'] = name if name != "" else consumerFacebookId['name']
        consumer=updateConsumerById(consumerFacebookId['id'], consumerFacebookId)
        return consumer
    elif(consumerEmail):
        consumerEmail['phone'] = phone if phone != "" else consumerEmail['phone']
        consumerEmail['facebookId'] = facebookId if facebookId != "" else consumerEmail['facebookId']
        consumerEmail['name'] = name if name != "" else consumerEmail['name']
        consumer=updateConsumerById(consumerEmail['id'], consumerEmail)
        return consumer
    else:
        consumer = {
            "id": generateUUID(),
            "email": email if email != "" else None,
            "phone": phone if phone != "" else None,
            "facebookId": facebookId if facebookId != "" else None,
            "name": name if name != "" else None,
            "consumerDataStore": None
        }
        consumers.append(consumer)

        with open(APP_PATH + '/data/consumers.json', 'w') as outfile:
            json.dump(consumers, outfile)
            outfile.close()

        return consumer
