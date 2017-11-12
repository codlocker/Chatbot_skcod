# encoding: utf-8
import random
import helper_functions
import facebook_json_creators
# import newrelic.agent
# import api.controllers
# newrelic.agent.initialize(api.controllers.newrelic_file_path)

def text_parser(value,id):
    return {'text':value[id]}


def button_parser(value,id):
    x = {'attachment':{'type':'template','payload':{'template_type':'button','text':value[id]['text'],'buttons':value[id]['button']}}}
    return x

def file_parser(value,id):
    return {'attachment':{'type':'file','payload':{'url':value[id]['url']}}}

def image_parser(value,id):
    return {'attachment':{'type':'image','payload':{'url':value[id]['url']}}}

def audio_parser(value,id):
    return {'attachment':{'type':'audio','payload':{'url':value[id]['url']}}}

def video_parser(value,id):
    return {'attachment':{'type':'video','payload':{'url':value[id]['url']}}}

def key_parser(key,value,id,platform):
    if platform == 'facebook':
        return facebook_json_creators.create_json(key,value[id])['message']
    # return value[id]

def json_validator(key,value,platform):
     return helper_functions.final_validator(key,value,platform)

# @newrelic.agent.background_task(name='facebook_parser_final')
def facebook_parser_final(facebook_entries):
    final_result = []
    keys = ['generic_template', 'boarding_pass', 'receipt', 'list', 'check_in', 'itinerary', 'update', 'quick_reply',
            'button_template']
    size = 0
    for entry in facebook_entries:
        for key in entry:
            for i in entry[key]:
                json_validation = json_validator(key,i,'facebook')
                if json_validation == 0:
                    return 'check ' + key + ' in ' + str(entry)
    for entry in facebook_entries:
        for key in entry:
            size = len(entry[key])
            break
        break
    random_int = random.randint(0,size-1)
    for entry in facebook_entries:
        for key in entry:
            if key == 'text':
                final_result.append(text_parser(entry[key],random_int))
            elif key == 'audio':
                final_result.append(audio_parser(entry[key],random_int))
            elif key == 'video':
                final_result.append(video_parser(entry[key],random_int))
            elif key == 'image':
                final_result.append(image_parser(entry[key],random_int))
            elif key == 'file':
                final_result.append(file_parser(entry[key],random_int))
            elif key == 'quick_reply':
                final_result.append(entry[key][random_int])
            elif key == 'button_template':
                final_result.append(button_parser(entry[key], random_int))
            elif key in keys:
                final_result.append(key_parser(key,entry[key],random_int,'facebook'))
    return final_result


