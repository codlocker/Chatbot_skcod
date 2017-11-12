from flask import jsonify, request
from api import app, APP_PATH
from copy import deepcopy
import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)-6s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

import json

import api.bot.df_rules as dfr
import api.bot.generation_rules as gr
import api.bot.generation_templates as gt

# from api.bot import df, df_rules, generation_rules, generation_templates
from api.libraries.execute_python import runCode,generateUUID,checkSantityAndUpdateDemandFrame
from api.libraries.constants import pipeline
from api.libraries.intelligence_engine_request import getNLPData
from api.libraries.gentemplateparsers.parser import final_validation

from api.data.room import createRoom, getRoomById, updateRoom
from api.data.message import createMessage, getMessageById, updateMessage
from api.data.consumer import createConsumer, updateConsumerById
from api.data.custom_ners import getCustomNers, getCustomNersFromServer

# This code will run your code and will have some sample variables whose values can be tweaked to simulate the similar behaviour as in production pipeline.
# The pipeline output assumed now will be stored in nlp.py
# The constants will be stored in constants.py:
#     consumerData
#     lastdfState?
#     newdfState?
#     dataStore?
#     messageStore?
#     databases?
#     customNers?

@app.route("/send", methods=['POST'])
def send():
    content=request.get_json()
    queryData= {
        "room_id": content.get("room_id", None),
        "msg": content.get("msg", None),
        "type": content.get("type", "human"),
        "consumer": content.get("consumer", {"email": "batman@gotham.com", "name": "Batman"}),
        "platform": content.get("platform", "web")
    }
    # print queryData
    logger.debug('Input To The API:')
    logger.debug(queryData)
    logging.info('\n')
    resultRoom=None
    resultMessage=None
    botMessage=None
    nersMessage=None
    botData=None
    pipelineData=None
    demand_frames=None
    new_df=None
    message=None
    template_key=None
    generation_output=None
    generation_msg=None
    resultUpdateRoom=None
    resultUpdateMessage=None
    consumerData=None
    databases=None
    variables=None # variables to be passed to DF Rules, Generation Rules.
    dataStore=None # variable used to store values retrieved in DF rules/Gen Rules via api calls or generated variables, to be used in Gen Templates.
    consumerDataStore=None

    consumerData=createConsumer(queryData['consumer'])

    # print consumerData, "Checkpoint 3"
    logger.debug("Consumer Data")
    logger.debug(consumerData)
    logging.info('\n')

    queryData['consumer_id']=consumerData['id']

    if(queryData['room_id']):
        resultRoom=getRoomById(queryData['room_id'])
    else:
        with open(APP_PATH + '/bot/df.py', 'r') as myfile:
            data=myfile.read()
            resultRoom=createRoom(consumerData, data)

    logger.debug("Room State At The Start Of the Message")
    logger.debug(resultRoom)
    logging.info('\n')
    # print resultRoom, "Room Fetched"

    if(queryData['msg']):
        messageDict = {
            "id": generateUUID(),
            "roomId": resultRoom['id'],
            "consumer": consumerData,
            "userType": queryData['type'],
            "message": queryData['msg'],
            "messageStore": None
        }
        # print messageDict, "Checkpoint 7"
        resultMessage=createMessage(messageDict)
        logger.debug("Message Created")
        logger.debug(resultMessage)
        logging.info('\n')
        # print resultMessage, "Checkpoint 8"
    else:
        # print "No message was sent", "Checkpoint 9"
        logger.error("No message was sent")
        logging.info('\n')
        return jsonify({"room": resultRoom, "generated_msg": "Can you please pardon, I did not get any message."})

    # custom_ners=getCustomNers()
    # UNCOMMENT THIS WHEN SERVERS ARE BACK UP.
    custom_ners=getCustomNersFromServer()
    # logger.debug("Custom Ners From Server")
    logger.debug("Custom Ners From Local")
    logger.debug(custom_ners)
    logging.info('\n')
    # print custom_ners, "Checkpoint 10"

    if(queryData['type'] == 'human'):
        new_ners=custom_ners['new_ners']
        databases=custom_ners['databases']
        # print new_ners, databases, "Checkpoint 11"

        pipelineData=getNLPData(pipeline, queryData['msg'], new_ners)
        # print pipelineData, "Checkpoint 12"

        variables={}
        variables['nlp']=pipelineData['inputParams']
        variables['databases']=databases
        variables['lastdfState']=resultRoom['dfState']
        variables['dataStore']=resultRoom['dataStore'] if 'dataStore' in resultRoom else None
        variables['consumerDataStore']=consumerData['consumerDataStore'] if 'consumerDataStore' in consumerData else None
        consumerData.pop('consumerDataStore', None)
        variables['consumerData']=consumerData
        # print variables, "checkpoint 13"
        logger.debug("Variables Provided by Platform")
        logger.debug(variables)
        logging.info('\n')

        # Run DF Rules to get new df state.
        new_df = {}
        # with open(APP_PATH + '/bot/df_rules.py', 'r') as myfile:
            # data=myfile.read()
            # extdata.variables = deepcopy(variables)
            # outputdfRules = runCode(data, variables)
        outputdfRules = dfr.main_function(deepcopy(variables))
        # print outputdfRules, "Checkpoint 14"
        logger.debug("Output after running DF Rules")
        logger.debug(outputdfRules)
        logging.info('\n')

        if('df' in outputdfRules): # If df key is present in output dict of df rules then set newuser_df to it, else set new_df to old df. This is done so that our code doesn't fail.
            new_df = outputdfRules['df']
            new_df = checkSantityAndUpdateDemandFrame(variables['lastdfState'], new_df)
        else:
            new_df = variables['lastdfState']
#
        # print new_df, "checkpoint 15"
        logger.debug("New DF State")
        logger.debug(new_df)
        logging.info('\n')
#
        if('dataStore' in outputdfRules): # Creating only one output dfRules allows user to access the same third party urls and access data across all df value, this leads to faster execution, better code sharing between different logic silos, but can lead to errors if the developer is not careful with their output. This error should be handled in future by checking keys in new df and lastdfstate. Skipping for now.
            variables['dataStore']=outputdfRules['dataStore']

        if('consumerDataStore' in outputdfRules):
            variables['consumerDataStore']=outputdfRules['consumerDataStore']
#
        resultRoom['dfState'] = new_df
        # print resultRoom, "checkinpoint 16"
        logger.debug("Room State After DF Rules")
        logger.debug(resultRoom)
        logging.info('\n')
        # Now that we have the new DF state, we need to run Gen Rules
        variables['newdfState'] = new_df
        # print variables['newdfState'], "checkinpoint 17"
        logger.debug("Variables After DF Rules")
        logger.debug(variables)
        logging.info('\n')
#
        # Run Gen rules with new Df state and variables.
        # with open(APP_PATH + '/bot/generation_rules.py', 'r') as myfile:
        #     data=myfile.read()
        #     # outputGenerationRules = runCode(data, variables)
        outputGenerationRules = gr.main_function(deepcopy(variables))
        # print outputGenerationRules, "checkpoint 18"
        logger.debug("Output After Running Generation Rules")
        logger.debug(outputGenerationRules)
        logging.info('\n')

        if('dataStore' in outputGenerationRules):
            variables['dataStore'] = outputGenerationRules['dataStore']

        if('consumerDataStore' in outputGenerationRules):
            variables['consumerDataStore'] = outputGenerationRules['consumerDataStore']
#
        if('messageStore' in outputGenerationRules):
            variables['messageStore'] = outputGenerationRules['messageStore']
        else:
            variables['messageStore'] = {}
#
        if('templateKey' in outputGenerationRules):
            template_key = outputGenerationRules['templateKey']
            variables['templateKey'] = template_key
#
            # Now that we have the key and we have the updated dataStore value, we can pass this data to run GenerateTemplates Code and get the output template code.
            # with open(APP_PATH + '/bot/generation_templates.py', 'r') as myfile:
                # data=myfile.read()
            if variables['templateKey'] == 'commonsense' and 'commonsense' in variables['nlp'].keys() and 'tag' in \
                    variables['nlp']['commonsense'].keys():
                outputGenerationTemplates = [{'text': variables['nlp']['commonsense']['value']}]
            else:
                # outputGenerationTemplates = runCode(data, variables)
                outputGenerationTemplates = gt.main_function(deepcopy(variables))
            # print outputGenerationTemplates, "checkpoint 19"
            logger.debug("Output After Running Generation Templates")
            logger.debug(outputGenerationTemplates)
            logging.info('\n')
            generation_msg = final_validation(outputGenerationTemplates, queryData['platform'])
        else:
            generation_msg = 'I am sorry, I did not understand your query'
    #
    #         # NOTE:
    #         # All values like endflow, sendtoagent etc, will be added to messageStore of a bot message.
    #         # In case of send to agent, in the generation rules, the user can send the chats to imichat or other platform.
    #         # In case of integration with connect, the user can set values of endflow and sendtoagent to true in messageStore
    #

        logger.debug("Generation Message")
        logger.debug(generation_msg)
        logging.info('\n')

        # updateConsumer
        variables['consumerData']['consumerDataStore'] = variables['consumerDataStore']
        consumerData=updateConsumerById(consumerData['id'], variables['consumerData'])

        # updateRoom
        resultRoom['dataStore'] = variables['dataStore']

        roomUpdateDict = {
            "consumer": consumerData,
            "dfState": resultRoom['dfState'],
            "dataStore": resultRoom['dataStore']
        }

        logger.debug("Room Data Store")
        logger.debug(resultRoom['dataStore'])
        logging.info('\n')

        logger.debug("Consumer Data Store State")
        logger.debug(variables['consumerDataStore'])
        logging.info('\n')

        resultRoom = updateRoom(resultRoom['id'], roomUpdateDict)

        logger.debug("Room State After The Current Message")
        logger.debug(resultRoom)
        logging.info('\n')
        # print generation_msg, resultRoom, "checkpoint 20"
        # updateMessage
        messageUpdateDict = {
            "generatedDf": resultRoom['dfState']
        }
        if(queryData['platform'] == 'web' or queryData['platform'] == 'alexa'):
            messageUpdateDict['generatedMsgString'] = generation_msg
        else:
            messageUpdateDict['generatedMsg'] = generation_msg
        resultMessage = updateMessage(resultMessage['id'], messageUpdateDict)
        botMessageDict = {
            "id": generateUUID(),
            "roomId": resultRoom['id'],
            "consumerId": consumerData,
            "userType": "bot",
            "message": generation_msg,
            "messageStore": variables['messageStore'] if ('messageStore' in variables) else None
        }
        botMessage = createMessage(botMessageDict)
    #
    #
    #         # return the response to the send API
        returnDictionary = {
            "room": resultRoom,
            "generated_msg": generation_msg,
            "templateKey": variables["templateKey"] if "templateKey" in variables.keys() else "",
            "sendtoagent": True if ('sendtoagent' in variables['messageStore'] and variables['messageStore']['sendtoagent']) else False
        }

        logger.debug("Final Output")
        logger.debug(returnDictionary)
        logging.info('\n')

        return jsonify(returnDictionary)
    #
    else:
        # message was added to room and db now since this is bot, no need to generate a new message, return back to user.
        # print "Checkpoint 10", resultRoom
        logger.debug("Room State After Bot Message Is Sent")
        logger.debug(resultRoom)
        logging.info('\n')
        return jsonify({"room": resultRoom, "generated_msg": None})
    #
    # except Exception as e:
    #     print("Internal Server Error Occured: ", e)
    #     return jsonify({"message": "Internal Server Error"})
