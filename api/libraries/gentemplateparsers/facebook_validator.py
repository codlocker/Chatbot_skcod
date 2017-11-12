from __init__ import *


generic = {typee:dict,req:{"elements":{typee:list,objects_list:{req:{'title':{typee:string}},
                                                                notreq:{'subtitle':{typee:string},
                                                                        'image_url':{typee:string},
                                                                        'buttons':{validators:['buttons']}}}}}}
list_temp = {typee:dict,
             req:{"button":{validators:['buttons']},"elements":{typee:list,objects_list:{req:{'title':{typee:string}},
                notreq:{'subtitle':{typee:string},'image_url':{typee:string},'button':{validators:['buttons']}}}}}}
receipt = {typee:dict,req:{'recipient_name':{typee:string},"order_number":{typee:string},"currency":{typee:string},"payment_method":{typee:string},"order_url":{typee:string},"total_cost":{typee:floats}},notreq:{'subtotal':{typee:floats},'shipping_cost':{typee:floats},'total_tax':{typee:floats},'elements':{typee:list,objects_list:{req:{'title':{typee:string},'price':{typee:floats}},notreq:{'quantity':{typee:floats},'subtitle':{typee:string},'currency':{typee:string},'image_url':{typee:string}}}}}}
boarding_pass = {typee:dict,req:{'intro_message':{typee:string},'locale':{typee:string},'passengers':{typee:list,objects_list:{req:{
    'passenger_name': {typee:string},'pnr_number':{typee:string},'seat': {typee:string},'flight_number':{typee:string} ,
    'departure_time':{typee:string} ,'arrival_time':{typee:string},'boarding_time':{typee:string},
    'departure_airport':{req:{'airport_code':{typee:string},'city':{typee:string}}},
    'arrival_airport':{req:{'airport_code':{typee:string},'city':{typee:string}}
}},notreq:{'qr_code':{typee:string},'travel_class':{typee:string},'above_bar_code_image_url':{typee:string}}}}}}




check_in = {typee:dict,req:
    {'intro_message':{typee:string},'locale':{typee:string},'pnr_number':{typee:string},'checkin_url':{typee:string},'flight_info':{typee:list,objects_list:
        {req:{'departure_time':{typee:string} ,'arrival_time':{typee:string},'boarding_time':{typee:string},'departure_airport':{req:{'airport_code':{typee:string},'terminal':{typee:string},'gate':{typee:string},'city':{typee:string}}},'arrival_airport':{req:{'terminal':{typee:string},'gate':{typee:string},'airport_code':{typee:string},'city':{typee:string}}
}}}}}
            }
itinerary = {typee:dict,req:
    {'total_price':{typee:string},'intro_message':{typee:string},'locale':{typee:string},'pnr_number':{typee:string},
     'passengers':{typee:list,objects_list:{req:{'name':{typee:string},'passenger_id':{typee:string}},notreq:{'ticket_number':{typee:string}}}}
        ,'passenger_segment_info':
        {typee:list,objects_list:{req:{'passenger_id': {typee:string}, 'segment_id':{typee:string},'seat':{typee:string},'seat_type':{typee:string}}}},
     'flight_info':{typee:list,objects_list:{req:{'departure_airport':{req:{'airport_code':{typee:string},'terminal':{typee:string},'gate':{typee:string},'city':{typee:string}}},
                                    'arrival_airport':{req:{'terminal':{typee:string},'gate':{typee:string},'airport_code':{typee:string},'city':{typee:string}}
},'connection_id':{typee:string},'segment_id':{typee:string},'flight_number':{typee:string},'aircraft_type':{typee:string},'departure_time':{typee:string} ,'arrival_time':{typee:string}}}}

     },
             notreq:{'base_price':{typee:string},'tax':{typee:string},'currency':{typee:string}}}

update = {typee:dict,req:{'intro_message':{typee:string},'locale':{typee:string},'pnr_number':{typee:string},'update_type':{typee:string},'flight_number':{typee:string},'departure_time':{typee:string} ,'arrival_time':{typee:string},'boarding_time':{typee:string},'departure_airport':{req:{'airport_code':{typee:string},'terminal':{typee:string},'gate':{typee:string},'city':{typee:string}}},'arrival_airport':{req:{'terminal':{typee:string},'gate':{typee:string},'airport_code':{typee:string},'city':{typee:string}}
}}}

buttons = {
    'web_url':{req:{'type':{typee:string,values:['web_url']},'title':{typee:string},'url':{typee:string}},notreq:{'fallback_url':{typee:string}}},
        'postback':{req:{'type':{typee:string,values:['postback']},'title':{typee:string,max:20},'payload':{typee:string,max:1000}}},
    'call':{req:{'type':{typee:string,values:['phone_number']},'title':{typee:string,max:20},'payload':{typee:string}}},
    'share':{'type':{typee:string,values:['element_share']},},
    'buy':{req:{'type':{typee:string,values:['payment']},'title':{typee:string},'payload':{typee:string},'payment_summary':{
        req:{'price_list':{typee:list,objects_list:{req:{'label':{typee:string},'amount':{typee:string}}}},'requested_user_info':{typee:list,objects_list:{typee:string,values:['shipping_address','contact_name','contact_phone','contact_email']}},'currency':{typee:string},'merchant_name':{typee:string},'payment_type':{typee:string,values:['FIXED_AMOUNT','FLEXIBLE_AMOUNT']}},notreq:{'is_test_payment':{typee:boolean}}
    }}},
    'login':{req:{'type':{typee:string,values:['login']},'url':{typee:string}}},
    'logout':{req:{'type':{typee:string,values:['logout']},'url':{typee:string}}}

}

quick_replies = {'text':{req:{'content_type':{typee:string},'title':{typee:string,max:20},'payload':{'max':1000,typee:string}},notreq:{'image_url':{typee:string}}},
                 'location':{req:{'content_type':{typee:string}}}}

button_template = {typee:dict,req:{"text":{typee:string},"button":{typee:list}}}

data_mappings = {'receipt':receipt,'generic_template':generic,'list':list_temp,'itinerary':itinerary,'update':update,'check_in':check_in,'boarding_pass':boarding_pass,'quick_reply':quick_replies,'button_template':button_template}

# import json
# json.dumps(list_temp)