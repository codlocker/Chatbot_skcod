import inbuilt_validations
import copy
import facebook_parser,alexa_parser,web_parser
# import newrelic.agent
# import api.controllers
# newrelic.agent.initialize(api.controllers.newrelic_file_path)

reply_values = [{"text":["Hello there! I'm Ahana, wishing you and your loved ones a very Happy Diwali on behalf of Citibank"]},{"image":{"url":"https://s3.amazonaws.com/botsociety.prod.us/d82b7fb86fe6035f899dd_videopng.png (600kB) "}},{"include":["facebook"],                                                                                                                        "button_template":[{
           "type":"web_url",
           "url": "https://s3.amazonaws.com/botsociety.prod.us/ef9c8b28470f41c347b5641089d71_videopng.png (600kB) ",
            #"webview_height_ratio": "tall",
           # "messenger_extensions": True,
           "fallback_url": "https://s3.amazonaws.com/botsociety.prod.us/ef9c8b28470f41c347b5641089d71_videopng.png (600kB) "
       }],                                                                                                                          "quick_reply":[{
           "text":"I'm here to illuminate your Diwali with Citibank's sparkling offers",
           "quick_replies":[{
               "payload":"Dazzle me",
               "title":"Dazzle me",
               "content_type":"text"
           }]
       }]}
       ]



# reply_values = [{
# 	"generic_template": [{
# 		"elements": [{
# 				"image_url": "https://s3-us-west-2.amazonaws.com/barclaysfaqbot/barclays1.jpg",
# 				"button": [{
# 					"type": "postback",
# 					"title": "Cheque Related Queries",
# 					"payload": "cheque"
# 				}],
# 				"title": "Ask Now"
# 			},
# 			{
# 				"image_url": "https://s3-us-west-2.amazonaws.com/barclaysfaqbot/barclays2.jpg",
# 				"button": [{
# 					"type": "postback",
# 					"title": "Account Related Queries",
# 					"payload": "account"
# 				}],
# 				"title": "Ask Now"
# 			},
# 			{
# 				"image_url": "https://s3-us-west-2.amazonaws.com/barclaysfaqbot/barclays3.jpg",
# 				"button": [{
# 					"type": "postback",
# 					"title": "Payments or Transactions",
# 					"payload": "transaction"
# 				}],
# 				"title": "Ask Now"
# 			},
# 			{
# 				"image_url": "https://s3-us-west-2.amazonaws.com/barclaysfaqbot/barclays4.jpg",
# 				"button": [{
# 					"type": "postback",
# 					"title": "Direct Debits",
# 					"payload": "direct debit"
# 				}],
# 				"title": "Ask Now"
# 			},
# 			{
# 				"image_url": "https://s3-us-west-2.amazonaws.com/barclaysfaqbot/barclays5.jpg",
# 				"button": [{
# 					"type": "postback",
# 					"title": "Debit and Credit Cards",
# 					"payload": "credit"
# 				}],
# 				"title": "Ask Now"
# 			}
# 		]
# 	}]
# reply_values = [{'text': ['Hi', 'Hey']}]
# }]
# reply_values = [{'text': ['Hi', 'Hey']},
#                 {'audio':[{'url':'hi.mp3'},{'url':'hey.mp3'}]},
#                 {'video':[{'url':'welcome.mp4'}]},
#                 {'image':[{'url':'welcome.jpg'}]},
#                 {'file':[{'url':'url.now'}]},
#                 {'quick_reply':[
#                     {'text':'sf',
#                      'quick_replies':[{'content_type':'text','title':'sf','payload':''}]}]},
#                 {'delay': 10},
#                 {'list': [{
# 		'elements': [{
# 			'title': "",
# 			'subtitle': "",
# 			'image_url': "",
# 'button': {
# "type":"web_url",
# 			'url': "",
# 			'fallback_url': '',
# 			'title': ""
# 		}
# 		}],
# 		'button': {
#  "type":"postback",
# 			'payload':"",
# 			'title': ""
# 		}
# 	}]},
#                 {'receipt': [{
# 		'recipient_name': 'sfd',
# 		'order_number': 'os',
# 		'currency': '',
# 		'payment_method': 'df',
# 		'order_url':'sdf',
# 		'elements': [{
# 			'title': 'sf',
# 			'subtitle': 'sdf',
# 			'quanitity': 2,
# 			'price': 89,
# 			'currency': 'usd',
# 			'image_url': 'kdsjf'
# 		}],
#
#           "subtotal":75.00,
#           "shipping_cost":4.95,
#           "total_tax":6.19,
#           "total_cost":56.14
#
# 	}]},
#                 {'boarding_pass':[{'intro_message':"","locale":"sdf","passengers":[{"passenger_name":"sf","pnr_number":"","travel_class":"sdf","seat":"sdf","qr_code":"sdf","flight_number":"sf","departure_time":"df","arrival_time":"sdf","boarding_time":"sdf",'departure_airport':{"airport_code":"sf","city":"sf"},'arrival_airport':{"airport_code":"sf","city":"sf"}}]}]},
#                 {'generic_template': [{
#                         'elements': [{
#                             'title': "",
#                             'subtitle': "",
#                             'image_url': "",
#                             'button': [{'type':'element_share'}]
#                         }]
#
#                     }]},
#                 {'check_in':[{'intro_message':"sfd","locale":"sdf","pnr_number":"s","checkin_url":"sdf",'flight_info':[{'flight_number':'sf',"departure_airport":{"airport_code":"sfd","city":"sdf","terminal":"sdf","gate":"sdf"},"arrival_airport":{"airport_code":"sfd","city":"sdf","terminal":"sdf","gate":"sdf"},"boarding_time":"sf","arrival_time":"sf","departure_time":"sf"}]}]},
#                 {"update": [{
#         "intro_message": "dsf",
#         "update_type": "sf",
#         "locale": "sf",
#         "pnr_number": "sf",
#         "flight_number": "df",
#         "departure_airport": {
#             "airport_code": "SFO",
#             "city": "San Francisco",
#             "terminal": "T4",
#             "gate": "G8"
#         },
#         "arrival_airport": {
#             "airport_code": "AMS",
#             "city": "Amsterdam",
#             "terminal": "T4",
#             "gate": "G8"
#         },
#         "boarding_time": "2015-12-26T10:30",
#         "departure_time": "2015-12-26T11:30",
#         "arrival_time": "2015-12-27T07:30"
#     }]},
#                 { "itinerary": [{
#         "base_price": "sf",
#         "tax": "sf",
#         "currency": "sf",
#         "total_price": "sf",
#         "price_info": [
#             {
#                 "title": "sf",
#                 "amount": "sf",
#                 "currency": "sf"
#             }
#         ],
#         "intro_message": "sfa",
#         "locale": "df",
#         "pnr_number": "sf",
#         'passengers':[{'name':'sfd','passenger_id':"asdf"}],
#         "passenger_segment_info": [
#             {
#                 "segment_id": "s",
#                 "passenger_id": "s",
#                 "seat": "s",
#                 "seat_type": "d"
#             }
#         ],
#         "flight_info": [
#             {
#                 "connection_id": "sf",
#                 "segment_id": "sdf",
#                 "flight_number": "sf",
#                 "aircraft_type": "fs",
#                 "departure_airport": {
#                     "airport_code": "sf",
#                     "city": "sf",
#                     "terminal": "sf",
#                     "gate": "sf"
#                 },
#                 "departure_time": "sf",
#                 "arrival_time": "sf",
#                 "travel_class": "sf",
#                 "arrival_airport": {
#                     "airport_code": "sf",
#                     "city": "sf",
#                     "terminal": "sf",
#                     "gate": "sf"
#                 }
#             }
#         ]
#     }],"button_template": [{
# 		"text": "your text goes here",
# 		"button": [{
# 			"type": "type of the button",
# 			"title": "title of the button",
# 			"payload": "payload goes here"
# 		}]
# 	}]}
# ]
# reply_values = [{"delay":10}]
# reply_values =  [{
#  	"include": ["facebook", "web"],
#  	"text": "We're sorry to hear that!!"
#  }, {
#  	"include": ["facebook", "web"],
#  	"text": ["We are sorry to hear that! We'll cancel your card and send a replacement within 2 working days. Please remember to keep an eye out for unusual transactions on your statement and report to us immediately. You can choose one of the tabs to report a lost or stolen debit card."],
#  	"audio": [{
#  		"url": "https://ancient-fjord-82489.herokuapp.com/1_0.mp3"
#  	}],
#  	"video": [{
#  		"url": "https://storage.googleapis.com/barclays_faq/reportstolen.mp4"
#  	}],
#  	"quick_reply": {
#  		"text": "You can choose one of the tabs to report a lost or stolen debit card.",
#  		"quick_replies": [{
#  			"content_type": "text",
#  			"title": "Online",
#  			"payload": "lost card online"
#  		}, {
#  			"content_type": "text",
#  			"title": "Mobile",
#  			"payload": "lost card mobile"
#  		}, {
#  			"content_type": "text",
#  			"title": "Telephone",
#  			"payload": "lost card telephone"
#  		}, {
#  			"content_type": "text",
#  			"title": "Branch",
#  			"payload": "lost card branch"
#  		}]
#  	}
#  }]

# reply_values_copy = copy.copy(reply_values)


platforms_supported = ['facebook','slack','email','skype','web','alexa']
platform_supported_values = {
    'facebook' : ['button_template','text','audio','video','image','file','quick_reply',"generic_template","receipt","update","itinerary","check_in","boarding_pass","list"],
    'slack' : ['text','audio','video','image'],
    'email' : ['text'],'alexa' : ['text'],
    'skype' : ['image'],'web':['text']
}
validation_list = ['button_template','text','audio','image','video','file','quick_reply',"generic_template","receipt","update","itinerary","check_in","boarding_pass","list"]
validation_keyset = validation_list+['include','exclude']
reverse_platforms_supported = {}
inbuilt_tags = ['delay']
for key in validation_list:
    reverse_platforms_supported[key] = []
for key in validation_list:
    for platform in platform_supported_values:
        if key in platform_supported_values[platform]:
            reverse_platforms_supported[key].append(platform)

# @newrelic.agent.background_task(name='validation')
def validation(reply_values):
    reply_dict = {}
    for value in reply_values:
        if 'include' in value and 'exclude' in value:
            return 'please specify either include or exclude in ' + str(value)
        for key in value:
            if key not in validation_keyset:
                if key in inbuilt_tags:
                    if key == 'delay':
                        reply_values.remove(value)
                        ret = inbuilt_validations.delay_checker(value)
                        if ret != "ok":
                            return ret['message']
                else:
                    return 'please specify correct dictionary for ' + str(value)
    for platform in platforms_supported:
        if platform not in reply_dict:
            reply_dict[platform] = []
    for value in reply_values:
        present_platform = []
        if 'include' not in value and 'exclude' not in value:
            temp_platforms = []
            for key in value:
                if key in validation_list:
                    for pp in platform_supported_values:
                        if key in platform_supported_values[pp]:
                            temp_platforms.append(pp)
                        # else:
                        #     return key +' not supported for ' + pp
            present_platform = list(set(temp_platforms))
        else:
            if 'include' in value:
                if value['include'] == ['all']:
                    temp = []
                    for p in platforms_supported:
                        for key in value:
                            if key in validation_list:
                                if p in reverse_platforms_supported[key]:
                                    temp.append(p)
                                else:
                                    return key + ' not supported on ' + p
                    present_platform = list(set(temp))
                else:
                    temp = []
                    for p in value['include']:
                        for key in value:
                            if key in validation_list:
                                if p in reverse_platforms_supported[key]:
                                    temp.append(p)
                                else:
                                    return key + ' not supported on ' + p
                    present_platform = list(set(temp))

            else:
                present_platform = copy.copy(platforms_supported)
                for platform in value['exclude']:
                    present_platform.remove(platform)
                temp = []
                for p in present_platform:
                    for key in value:
                        if key in validation_list:
                            if p in reverse_platforms_supported[key]:
                                temp.append(p)
                            else:
                                return key + ' not supported on ' + p
                present_platform = list(set(temp))
        for platform in present_platform:
            temp_dict = {}
            for key in value:
                if key != 'include' and key != 'exclude':
                    temp_dict[key] = value[key]
            reply_dict[platform].append(temp_dict)
    for platform in reply_dict:
        size = 0
        for value in reply_dict[platform]:
            for key in value:
                if len(value[key]) > size:
                    if len(value[key]) == 1:
                        size = 1
                    else:
                        if size > 1:
                            return 'check the size of ' + str(value[key])
                        else:
                            size = len(value[key])
        reply_dictionary = []
        for item in reply_dict[platform]:
            print item
            for key in item:
                reply_dictionary.append({key:item[key]})
        reply_dict[platform] = reply_dictionary
        temp_list = []
        for value in reply_dict[platform]:
            temp_value = {}
            for key in value:
                temp_value[key] = value[key]
                if len(temp_value[key]) == 1:
                    for i in range(1,size):
                        temp_value[key].append(temp_value[key][0])
                temp_list.append(temp_value)
            reply_dict[platform] = temp_list
    return reply_dict

# @newrelic.agent.background_task(name='final_validation')
def final_validation(reply_values,platform):
    reply_values_copy = copy.copy(reply_values)
    reply_dict = validation(reply_values)
    return_list = []
    if platform == 'facebook':
        if type(reply_dict) == type(""):
            return reply_dict
        return_list = facebook_parser.facebook_parser_final(reply_dict['facebook'])
        return_list = inbuilt_validations.combiner(reply_values_copy, return_list)
    elif platform == 'web':
        if type(reply_dict) == type(""):
            return reply_dict
        return_list =  web_parser.web_parser_final(reply_dict['web'])
    elif platform == 'alexa':
        if type(reply_dict) == type(""):
            return reply_dict
        return_list = alexa_parser.alexa_parser_final(reply_dict['alexa'])
    return return_list
    # elif platform == 'sms':
    #     if type(reply_dict) == type(""):
    #         return reply_dict
    #     return web_parser.web_parser_final(reply_dict['web'])

# u = final_validation(reply_values,'facebook')
# print u
# print validation(reply_values)
