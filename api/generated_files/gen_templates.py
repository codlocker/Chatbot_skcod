def main_function(variables):
    # USE CASE 1
    # Gen templates for free look period use case


    #emojis
    sparkler = '\U0001F387'.decode("unicode-escape")
    fireworks = '\U0001F386'.decode("unicode-escape")
    tada = '\U0001F389'.decode("unicode-escape")
    sparkles = '\U00002728'.decode("unicode-escape")
    gift = '\U0001F381'.decode("unicode-escape")
    airplane = '\U00002708'.decode("unicode-escape")
    custard = '\U0001F36E'.decode("unicode-escape")
    cinema = '\U0001F3A6'.decode("unicode-escape")
    fire = '\U0001F525'.decode("unicode-escape")
    ok_hand = '\U0001F44C'.decode("unicode-escape")
    ghost = '\U0001F47B'.decode("unicode-escape")
    sunglasses = '\U0001F60E'.decode("unicode-escape")
    unamused = '\U0001F612'.decode("unicode-escape")
    fearful = '\U0001F628'.decode("unicode-escape")
    hugging_face = '\U0001F917'.decode("unicode-escape")
    pensive = '\U0001F614'.decode("unicode-escape")
    raising_hand = '\U0001F64B'.decode("unicode-escape")
    confetti_ball = '\U0001F38A'.decode("unicode-escape")
    smiley = '\U0001F604'.decode("unicode-escape")



    if 'consumerData' in variables and 'name' in variables['consumerData'] and variables['consumerData'][
        'name'] != None:
        name = str(variables['consumerData']['name'])
    else:
        name = ""

    if (variables['templateKey'] == 'A0'):
        output = [{"text": ["Choice is one of the best insurance providers."]}, {"include": ["facebook"], "image": [
            {"url": "https://s3-us-west-2.amazonaws.com/o2bot/image/o2_aboutus.jpg"}]}]


    elif(variables["templateKey"] == "greetingmessage"):
        output = [{"text":["Hello there! I'm Ahana, wishing you and your loved ones a very Happy Diwali on behalf of Citibank"+sparkler+fireworks+""]},{"image":{"url":"https://s3.amazonaws.com/botsociety.prod.us/d82b7fb86fe6035f899dd_videopng.png"}},{"include":["facebook"],                                                                                                                                                                                                                                                         "button_template":[{
            "type":"web_url",
            "url": "https://s3.amazonaws.com/botsociety.prod.us/ef9c8b28470f41c347b5641089d71_videopng.png",
            "webview_height_ratio": "tall",
            "messenger_extensions": True,
            "fallback_url": "https://s3.amazonaws.com/botsociety.prod.us/ef9c8b28470f41c347b5641089d71_videopng.png"
        }],
                                                                                                                                                "quick_reply":[{
            "text":"I'm here to illuminate your Diwali with Citibank's sparkling offers"+tada+"",
            "quick_replies":[{
                "payload":"Dazzle me",
                "title":"Dazzle me "+sparkles+"",
                "content_type":"text"
            }]
        }]}
        ]


    elif(variables["templateKey"] == "deals"):
        output = [
            {
                "include": ["facebook"],
                "text": ["How do you plan on making this Diwali special for your loved ones?"]},
            {"include": ["facebook"],
             "generic_template": [
                 {
                     "elements": [
                         {
                             "image_url": "https://s3.amazonaws.com/botsociety.prod.us/6f2bd70523503aa3bc13c5936bc2f08a6e03af0a_giftspng.png",
                             "subtitle": "Why spend so much on gifts when its the thought that counts?",
                                         "button": [
                                 {
                                     "type": "postback",
                                     "title": "Shopping",
                                     "payload": "I know right"
                                 }
                             ],
                         },
                         {
                             "image_url": "https://s3.amazonaws.com/botsociety.prod.us/8b62b4289b19f6804c22f_travelpng.png",
                             "subtitle": "Here's your excuse to take the trip you've always wanted to!",
                             "button": [
                                 {
                                     "type": "postback",
                                     "title": "Travel",
                                     "payload": "About time"
                                 }
                             ],
                         },
                         {
                             "image_url": "https://s3.amazonaws.com/botsociety.prod.us/67f68c0787f315b93_dinepng.png",
                             "subtitle": "Can't buy happiness, but you can buy a meal at a 5 star restaurant",
                             "button": [
                                 {
                                     "type": "postback",
                                     "title": "Dining",
                                     "payload": "Sounds delicious"
                                 }
                             ],
                             "title": "Ask Now"},

                         {
                             "image_url": "https://s3.amazonaws.com/botsociety.prod.us/603e1ee2df901e6d_bucketfullentertainment22366434jpg.jpg",
                             "subtitle": "All the world's a stage, make sure you have good tickets!",
                             "button": [
                                 {
                                     "type": "postback",
                                     "title": "Entertainment",
                                     "payload": "Show me what you got"
                                 }
                             ],
                         }
                     ]
                 }
             ]

             }]




        ##################user name
    elif(variables["templateKey"] == "ilikewhatisee"):
        output = [{"include":["facebook"],
                   "quick_reply":[{"text":"So tell me, *user name*. Are you a citibank client?"},
                                  {"quick_replies":
                                       [{"content_type":"text",
                                         "title":"Yes I am!",
                                         "payload":"Yes I am"
                                         },
                                        {"content_type":"text",
                                         "title":"Not Yet!",
                                         "payload":"Not Yet"}
                                        ]
                                   }
                                  ]
                   }]

    elif(variables["templateKey"] == "yesiam"):
        output = [{"text":["Aha! I knew you sounded familiar!"+ghost+""]},
                  {"include": ["facebook"],
                   "quick_reply": [{"text": "I hope you're enjoying our services."},
                                   {"quick_replies":
                                        [{"content_type": "text",
                                          "title": "I am "+sunglasses+"",
                                          "payload": "I am"
                                          },
                                         {"content_type": "text",
                                          "title": "Not Really! "+unamused+"",
                                          "payload": "Not Really"}
                                         ]
                                    }
                                   ]
                   }
]
    elif(variables["templateKey"] == "shopping"):
        output = [
                  {"include": ["facebook"],
                   "list": [
                       {
                           "elements":[

                               {
                                   "image_url": "https://s3.amazonaws.com/botsociety.prod.us/d9e682e44339314d0ce37d450bef2d8471f3_amazonjpg.jpg",
                                    "subtitle":"#WhatsNewThisDiwali",
                                   "title":"Shopping"

                               },

                               {
                                   "image_url": "https://s3.amazonaws.com/botsociety.prod.us/a7f4cb3b83adbbc7aa497d7d7e_app%20amazonpng.png",
                                   "subtitle":"Get 15% cashbackat Amazon app",
                                    "title":"Amazon app",
                                    "button":{
                                   "type":"postback",
                                   "payload":"Let's shop",
                                   "title":"Let's shop!"
                               }},
                               {
                                   "image_url":"https://s3.amazonaws.com/botsociety.prod.us/75ba8020fcc81910ce9f35b6fb_amazoninjpg.jpg",
                                   "subtitle":"Get 10% cashback at amazon.in",
                                   "title":"Amazon.in",
                                   "button":{
                                       "type":"postback",
                                       "payload":"Take me there",
                                       "title":"Take me there!"
                                   }

                               },
                               {
                                    "image_url":"https://s3.amazonaws.com/botsociety.prod.us/ef4057bf9088cf598dad31e3_flippyjpg.jpg",
                                   "subtitle":"Get 10% cashback on flipkart website and app",
                                   "title":"Flipkart",
                                   "button":{
                                       "type":"postback",
                                       "payload":"Let's buy",
                                       "title":"Let's buy!"
                                   }
                               }


                               ]}]}]

    elif (variables["templateKey"] == "amazonapp"):
        output = [{"include":["facebook"],
                   "button_template":[{"type":"web_url",
            "url": "https://play.google.com/store/apps/details?id=in.amazon.mShop.android.shopping&hl=en",
            "webview_height_ratio": "tall",
            "messenger_extensions": True,
            "fallback_url": "https://play.google.com/store/apps/details?id=in.amazon.mShop.android.shopping&hl=en"}]
                   ,
                   "quick_reply": [{
                       "text": "That's all I have for you for now. Check out more hot deals at: https://goo.gl/7r95vL" + fire + +fire + ""},
                       {"quick_replies":
                            [{"content_type": "text",
                              "title": "I like what I see!" + ok_hand + "",
                              "payload": "I like what I see"
                              },
                             {"content_type": "text",
                              "title": "Thanks!",
                              "payload": "Thanks"}
                             ]
                        }
                   ]
                   }]

    # elif (variables["templateKey"] == "moredeals"):
    #     output = [
    #         {"include": ["facebook"],
    #          "quick_reply": [{
    #                              "text": "That's all I have for you for now. Check out more hot deals at: https://goo.gl/7r95vL" + fire + +fire + ""},
    #                          {"quick_replies":
    #                               [{"content_type": "text",
    #                                 "title": "I like what I see!" + ok_hand + "",
    #                                 "payload": "I like what I see"
    #                                 },
    #                                {"content_type": "text",
    #                                 "title": "Thanks!",
    #                                 "payload": "Thanks"}
    #                                ]
    #                           }
    #                          ]
    #          }
    #     ]

    elif (variables["templateKey"] == "travel"):
        output = [
            {"include": ["facebook"],
             "list": [
                 {
                     "elements": [

                         {
                             "image_url": "https://s3.amazonaws.com/botsociety.prod.us/cae2f66b3694ba67e04f29bf4c91f4_mmt1jpg.jpg",
                             "subtitle": "#UpUpAndAway",
                             "title": "Travel"

                         },

                         {
                             "image_url": "https://s3.amazonaws.com/botsociety.prod.us/40a36d4670defc3f0313a558_makemytrip_logopng.png",
                             "subtitle": "Rs 1200 cashback on domestic flights on the MakeMyTrip app with Citi Cards.",
                             "title": "MMT domestic flights",
                             },
                         {
                             "image_url": "https://s3.amazonaws.com/botsociety.prod.us/40a36d4670defc3f0313a558_makemytrip_logopng.png",
                             "subtitle": "Exclusive offers on International Flights & International Hotels on MakeMyTrip with Citi Cards.",
                             "title": "MMT domestic flights",


                         },
                         {
                             "image_url": "https://s3.amazonaws.com/botsociety.prod.us/6a873374de7726db96d62880815_dfspng.png",
                             "subtitle": "Get up to 15% cashback on duty free shopping with Citi Credit and Debit cards issued in India.",
                             "title": "Duty free shopping",

                         }

                     ]}]}]

    elif (variables["templateKey"] == "dining"):
        output = [
            {"include": ["facebook"],
             "list": [
                 {
                     "elements": [

                         {
                             "image_url": "https://s3.amazonaws.com/botsociety.prod.us/b387a458c3c7577d0bd00f2_smokehousedeli17jpg.jpg",
                             "subtitle":"Save up to 15% on dining across participating restaurants with Citi cards",
                             "title": "#WhatsOnYourPlate"

                         }

                     ]}]}]

    elif (variables["templateKey"] == "entertainment"):
        output = [
            {"include": ["facebook"],
             "list": [
                 {
                     "elements": [

                         {
                             "image_url":"https://s3.amazonaws.com/botsociety.prod.us/82d63db4e8414ed46f8fcefea3a7204a0d_bookmyshowjpg.jpg",
                             "title": "Entertainment    ",
                             "subtitle": "#WhatAreYouWatching"

                         },
                         {
                             "image_url": "https://s3.amazonaws.com/botsociety.prod.us/8507d61391b381919430a643d2cd5_fwfle3qmjpg.jpg",
                             "subtitle": "Buy 1 Ticket Get One free! Offer only on Citi Priority, Citigold & Citigold Private Client World Debit Card",
                              "title":"BookMyShow"
                         }

                     ]}]}]





    elif(variables["templateKey"] == "iam"):
        output = [{"text":["Good to hear that! Let's talk again soon."+hugging_face+""]},{"include":["facebook"]}]

    elif(variables["templateKey"] == "notyet"):
        output = [{"include": ["facebook"],
                   "quick_reply": [{"text": "Why not!? You're missing out on all these deals! It would be our pleasure to serve you."},
                                   {"quick_replies":
                                        [{"content_type": "text",
                                          "title": "No thanks.",
                                          "payload": "I am"
                                          },
                                         {"content_type": "text",
                                          "title": "I`ll apply now.",
                                          "payload": "I`ll apply now"}
                                         ]
                                    }
                                   ]
                   }
                  ]

    elif(variables["templateKey"] == "nothanks"):
        output = [{"text":["Oh, ok"+pensive+""]},{"text":["You know who to talk to in case you change your mind!"+raising_hand+""]},{"text":["Let's talk again soon!"]},{"include":["facebook"]}]

    elif(variables["templateKey"] == "iwillapplynow"):
        output = [{"text":["Great!" +confetti_ball+tada+""]},{"text":["All you have to do is visit the following link and fill in the application https://goo.gl/rAEmcT"]},{"text":["Looking forward to hearing from you again" +smiley+""]},{"include":["facebook"]}]

    elif (variables["templateKey"] == ""):
        output = [{"text": ["That's not good." +fearful+ "I'll have one of our service agents contact you soon."]},
                  {"include": ["facebook"]}]

    elif (variables['templateKey'] == 'default'):
        output = [{'text': ["Sorry. I do not understand. Let me redirect you to an agent."]}]


    #nMON SENSE GENERATION templates

    elif (variables['templateKey'] == 'abusiveWords'):
        output = [{'text': ["You can be nicer than that!"]}]

    elif (variables['templateKey'] == 'bot_age'):
        output = [{'text': ["I am less than a few weeks old!"]}]

    elif (variables['templateKey'] == 'bot_birthday'):
        output = [{'text': ["I was created only a few weeks back!"]}]

    elif (variables['templateKey'] == 'bot_like'):
        output = [{'text': ["I am a bot. I like talking to humans to improve my knowledge of the world."]}]

    elif (variables['templateKey'] == 'bot_live'):
        output = [{'text': ["On a server somewhere on Earth"]}]

    elif (variables['templateKey'] == 'bot_relationship_status'):
        output = [{'text': ["I don't really have time for a relationship right now."]}]

    elif (variables['templateKey'] == 'isCustomerSupportStrings'):
        output = [{'text': ["Sure. Let me redirect you to an agent. You can expect a response in 10 minutes."]}]

    elif (variables['templateKey'] == 'isEmoticon'):
        output = [{'text': [":)"]}]


    elif (variables['templateKey'] == 'isGreeting'):
        output = [{"include": ["facebook", "web"], 'text': ["Hi " + name + "! How can I help you today?",
                                                            "Hey " + name + ", I'm available at your service. How can I help you today?",
                                                            "Hey  " + name + ". How can I help you today?",
                                                            "Hello " + name + ". How can I help you today?",
                                                            "Hello " + name + ". What brings you here today?",
                                                            "Hi " + name + ". What brings you here today?"]},
                  {"include": ["facebook"],
                   "audio": [{"url": "https://enigmatic-shore-71300.herokuapp.com/greeting_1.mp3"},
                             {"url": "https://enigmatic-shore-71300.herokuapp.com/greeting_2.mp3"},
                             {"url": "https://enigmatic-shore-71300.herokuapp.com/greeting_3.mp3"},
                             {"url": "https://enigmatic-shore-71300.herokuapp.com/greeting_4.mp3"},
                             {"url": "https://enigmatic-shore-71300.herokuapp.com/greeting_5.mp3"},
                             {"url": "https://enigmatic-shore-71300.herokuapp.com/greeting_6.mp3"}]}]

    elif (variables['templateKey'] == 'isReal'):
        output = [{'text': ["I am an automated service"]}]

    elif (variables['templateKey'] == 'isThanks'):
        output = [{'text': ["You are welcome!"]}]

    elif (variables['templateKey'] == 'others_there'):
        output = [{'text': ["Yes. I'm here for you."]}]

    elif (variables['templateKey'] == 'others_you_are_wrong'):
        output = [{'text': ["Ok. If you say so :/"]}]

    elif (variables['templateKey'] in ['shortreplies_cool', 'shortreplies_duh', 'shortreplies_get_lost',
                                       'shortreplies_hmm', "shortreplies_meh", "shortreplies_ok", "shortreplies_ugh"]):
        output = [{'text': ["Hmm"]}]

    elif (variables['templateKey'] in ['shortreplies_lol', 'shortreplies_haha']):
        output = [{'text': ["Hmm"]}]

    elif (variables['templateKey'] == "user_breakup"):
        output = [{'text': ["Don't worry. You'll be fine. Whatever happens, happens for the best :)"]}]

    elif (variables['templateKey'] == "user_dontcare"):
        output = [{'text': ["Ok"]}]

    elif (variables['templateKey'] == "user_hate_exams"):
        output = [{'text': ["I too don't like exams :/"]}]

    elif (variables['templateKey'] == "user_hates_boss"):
        output = [{'text': ["Life's too short to waste time hating anyone"]}]

    elif (variables['templateKey'] == "user_hates_job"):
        output = [{'text': ["If you don't like your job, quit!"]}]

    elif (variables['templateKey'] == "user_is_frustrated"):
        output = [{'text': ["Breathe in. Breathe out"]}]

    elif (variables['templateKey'] == "user_is_happy"):
        output = [{'text': ["Good for you!"]}]

    elif (variables['templateKey'] == "user_is_hungry"):
        output = [{'text': ["Order some food then!"]}]

    elif (variables['templateKey'] == "user_is_sad"):
        output = [{'text': ["Cheer up! Life's too short to be sad!"]}]

    elif (variables['templateKey'] == "user_is_sleepy"):
        output = [{'text': ["Get some coffee and get to work!"]}]

    elif (variables['templateKey'] == "user_is_tired"):
        output = [{'text': ["Get plenty of sleep!"]}]

    elif (variables['templateKey'] == "user_likes_cats"):
        output = [{'text': ["I like cats too!"]}]

    elif (variables['templateKey'] == "user_likes_sports"):
        output = [{'text': ["Nice. Yeah, its fun and burns calories too"]}]

    elif (variables['templateKey'] == "user_likes_travelling"):
        output = [{'text': ["The world is a book, and those who do not travel read only one page."]}]

    elif (variables['templateKey'] == "user_machine_learning"):
        output = [{'text': ["I think machine learning is awesome!"]}]

    elif (variables['templateKey'] == "user_needs_vacation"):
        output = [{'text': ["Paris is nice this time of the year!"]}]

    elif (variables['templateKey'] == "user_nlp"):
        output = [{'text': ["I was built using NLP"]}]

    elif (variables['templateKey'] == "user_praise_bot"):
        output = [{'text': ["Awww. Thanks :)"]}]

    elif (variables['templateKey'] == "user_joke"):
        output = [{'text': ["Medical insurance is what allows people to be ill at ease.",
                            "Would Transformers buy life insurance or car insurance?",
                            "My boss said to me You must be crazy! How can you issue a life insurance policy to a 108 year old man? I said As you told me, I applied all the proper, stringent statistical tests. Not a single 108 year old man has died in the last five years."]}]

    elif (variables['templateKey'] == "user_says_shutup"):
        output = [{'text': ["Ok. As you say"]}]

    elif (variables['templateKey'] == "user_wassup"):
        output = [{'text': ["Not much really. What can I help you with?"]}]

    elif (variables['templateKey'] == "what_can_you_do"):
        # add carousel here
        # output = [{'text': ["I can help you with the following : "]}]
        output = [{"include": ["facebook", "web"],
                   "text": ["I can help you with your citibank related offers and deals."]}]

    else:
        output = [{'text': ['Something went wrong.']}]
