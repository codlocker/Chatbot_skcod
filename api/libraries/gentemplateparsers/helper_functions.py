import datetime
import babel
import re
from facebook_validator import *
import facebook_validator
all_ids = babel.localedata.locale_identifiers()
_rgbstring = re.compile(r'#[a-fA-F0-9]{6}$')

def minLength(obj,length):
    if len(obj) < length:
        return 0
    else:
        return 1

def maxLength(obj,length):
    if len(obj) > length:
        return 0
    else:
        return 1

def validatess(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%dT%H:%M')
        return 1
    except ValueError:
        return 0


def locale_validator(locale):
    if locale in all_ids:
        return 1
    return 0

def isrgbcolor(value):
    if bool(_rgbstring.match(value)):
        return 1
    return 0

def type_validator(object,typee):
    if typee == 'string':
        if type(object) == type('') or type(object) == type(u''):
            return 1
    if(type(object) == type(types[typee])):
        if typee == 'button':
            pass
        return 1
    return 0


def value_validator(value,values):
    if value in values:
        return 1
    return 0

def validate(arg,object,schema,platform):
    if arg == typee:
        return type_validator(object,schema[typee])
    elif arg == req:
        for key in schema[req]:
          if key not in object:
              return 0
        for key in schema[req]:
            aw = traverse(schema[req][key],object[key],platform)
            if aw == 0:
                return 0
        return 1
    elif arg == notreq:
        for key in schema[notreq]:
            if key in object:
                aaa = traverse(schema[notreq][key],object[key],platform)
                if aaa == 0:
                    return 0
        return 1
    elif arg == objects_list:
        return 1
    elif arg == max_list:
        return maxLength(object,schema['max_list'])
    elif arg == min_list:
        return minLength(object, schema['min_list'])
    elif arg == min:
        return minLength(object, schema['min'])
    elif arg == max:
        return maxLength(object,schema['max'])
    elif arg == values:
        return value_validator(object,schema[values])
    elif arg == 'validators':
        # return button_validator(object)
        if 'buttons' in schema['validators']:
            if platform == 'facebook':
                if facebook_button_validator(object) == 0:
                    return 0
            return 1
        if 'locale' in schema['validators']:
            if locale_validator(object) == 0:
                return 0
        if 'datetime' in schema['validators']:
            if validatess(object) == 0:
                return 0
        if 'theme' in schema['validators']:
            if isrgbcolor(object) == 0:
                return 0
        return 1
    return 0



def final_compare(uii,my_json,platform):
    return traverse(my_json,uii,platform)

def traverses(dict,user_dict,platform):
    if type(user_dict) == type(types[list]):
        if typee in dict:
            objectss = dict[objects_list]
            dict.pop(objects_list)
            for key in dict:
                bb = validate(key, user_dict, dict,platform)
                if bb == 0:
                    return 0

            for i in user_dict:
                gg = traverses(objectss, i,platform)
                if gg == 0:
                    return 0
        else:
            xx = 2
            pass


    for key in dict:
        if key == 'objects':
            xxxx = 6
        aa = validate(key, user_dict, dict,platform)
        if aa == 0:
            validate(key, user_dict, dict,platform)
            return 0
    return 1


def traverse(dict,user_dict,platform):
    if type(user_dict) == type(types[list]):
        if typee in dict:
            try:
                objectss = dict[objects_list]
            except:
                print 2
                pass
            for key in dict:
                bb = validate(key,user_dict,dict,platform)
                if bb == 0:
                    return 0

            for i in user_dict:
                gg = traverse(objectss,i,platform)
                if gg == 0:
                    traverse(objectss, i, platform)
                    return 0
        else:
            xx = 2
            pass
    for key in dict:
        if key == 'objects':
            pass
        aa = validate(key,user_dict,dict,platform)
        if aa == 0:
            validate(key, user_dict, dict,platform)
            # print 1
            return 0
    return 1

def final_validator(key,value,platform):
    if platform == 'facebook':
        if key in facebook_validator.data_mappings:
            if type(value) == type([]):
                if key == 'quick_reply':
                    for p in value:
                        for i in p['quick_replies']:
                            e = final_compare(i,facebook_validator.data_mappings[key][i['content_type']],platform)
                            if e == 0:
                                return 0
                elif key == 'button_template':
                    for i in value:
                        e = final_compare(i,facebook_validator.data_mappings[key],platform)
                        if e == 1:
                            for j in i['button']:
                                e = facebook_button_validator(j)
                                if e == 0:
                                    return 0
                        if e == 0:
                            return 0
                else:
                    return final_compare(value,facebook_validator.data_mappings[key],platform)
            return 1
        else:
            return final_compare(value,facebook_validator.data_mappings_global[key],platform)
    if platform == 'web':
        pass
    if platform == 'alexa':
        pass

####################################platform dependent validations



def facebook_button_validator(user_dict):
    tt = user_dict['type']
    ss = traverses(buttons[tt],user_dict,'facebook')
    return ss