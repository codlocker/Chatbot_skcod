import helper_functions
def create_json(key,value):
    if key == 'list':
        return create_for_list(value)
    if key == 'generic_template':
        return create_for_generic(value)
    if key == 'boarding_pass':
        return create_for_boarding(value)
    if key == 'update':
        return create_for_update(value)
    if key == 'itinerary':
        return create_for_itinerary(value)
    if key == 'check_in':
        return create_for_checkin(value)
    if key == 'receipt':
        return create_for_receipt(value)
    else:
        pass



def create_for_receipt(value):
    json_value = {}
    json_value['message'] = {}
    json_value['message']['attachment'] = {}
    json_value['message']['attachment']['type'] = 'template'
    json_value['message']['attachment']['payload'] = {}
    json_value['message']['attachment']['payload']['template_type'] = 'receipt'
    json_value['message']['attachment']['payload']['summary'] = {}
    for i in ['shipping_cost','subtotal','total_cost','total_tax']:
        if i in value:
            json_value['message']['attachment']['payload']['summary'][i] = value[i]
            value.pop(i)
    for i in value:
        json_value['message']['attachment']['payload'][i] = value[i]
    return json_value

def create_for_checkin(value):
    json_value = {}
    json_value['message'] = {}
    json_value['message']['attachment'] = {}
    json_value['message']['attachment']['type'] = 'template'
    json_value['message']['attachment']['payload'] = {}
    json_value['message']['attachment']['payload']['template_type'] = 'airline_checkin'
    for i in ['locale','intro_message','pnr_number','checkin_url']:
        json_value['message']['attachment']['payload'][i] = value[i]
    json_value['message']['attachment']['payload']['flight_info'] = value['flight_info']
    return json_value

def create_for_itinerary(value):
    json_value = {}
    json_value['message'] = {}
    json_value['message']['attachment'] = {}
    json_value['message']['attachment']['type'] = 'template'
    json_value['message']['attachment']['payload'] = {}
    json_value['message']['attachment']['payload']['template_type'] = 'airline_itinerary'
    for i in ['locale','intro_message','pnr_number']:
        json_value['message']['attachment']['payload'][i] = value[i]
    b = []
    for i in value['passengers']:
        y = {}
        for j in i:
            y[j] = i[j]
        b.append(y)
    json_value['message']['attachment']['payload']['passenger_info'] = b
    return json_value

def create_for_update(value):
    json_value = {}
    json_value['message'] = {}
    json_value['message']['attachment'] = {}
    json_value['message']['attachment']['type'] = 'template'
    json_value['message']['attachment']['payload'] = {}
    json_value['message']['attachment']['payload']['template_type'] = 'airline_update'
    for i in ['locale','intro_message','pnr_number','update_type']:
        json_value['message']['attachment']['payload'][i] = value[i]
    json_value['message']['attachment']['payload']['update_flight_info'] = {}
    for i in ['departure_airport','arrival_airport','flight_number']:
        json_value['message']['attachment']['payload']['update_flight_info'][i] = value[i]
    json_value['message']['attachment']['payload']['update_flight_info']['flight_schedule'] = {}
    for i in ['boarding_time','arrival_time','departure_time']:
        json_value['message']['attachment']['payload']['update_flight_info']['flight_schedule'][i] = value[i]
    return json_value

def create_for_boarding(value):
    json_value = {}
    json_value['message'] = {}
    json_value['message']['attachment'] = {}
    json_value['message']['attachment']['type'] = 'template'
    json_value['message']['attachment']['payload'] = {}
    json_value['message']['attachment']['payload']['template_type'] = 'airline_boardingpass'
    passengers = []
    for i in value['passengers']:
        kk = {}
        kk['arrival_airport'] = {}
        kk['arrival_airport']['city'] = i['arrival_airport']['city']
        kk['arrival_airport']['airport_code'] = i['arrival_airport']['airport_code']
        kk['departure_airport'] = {}
        kk['departure_airport']['city'] = i['departure_airport']['city']
        kk['departure_airport']['airport_code'] = i['departure_airport']['airport_code']
        for ui in i:
            kk[ui] = i[ui]
        if not ('qr_code' in i or 'above_bar_code_image_url' in i):
            return 'check qr_code and barcode'
        passengers.append(kk)
    json_value['message']['attachment']['payload']['passengers'] = passengers
    for i in ['intro_message','locale']:
        json_value['message']['attachment']['payload'][i] = value[i]
    return json_value

def create_for_generic(value):
    json_value = {}
    json_value['message'] = {}
    json_value['message']['attachment'] = {}
    json_value['message']['attachment']['type'] = 'template'
    json_value['message']['attachment']['payload'] = {}
    json_value['message']['attachment']['payload']['template_type'] = 'generic'
    d = []
    for i in value['elements']:
        temp = {}
        if 'image_url' in i:
            temp['image_url'] = i['image_url']
        if 'subtitle' in i:
            temp['subtitle'] = i['subtitle']
        temp['title'] = i['title']
        b = []
        for j in i['button']:
            b.append(create_for_button(j))
        temp['buttons'] = b
        d.append(temp)
    json_value['message']['attachment']['payload']['elements'] = d
    return json_value

def create_for_list(value):
    json_value = {}
    json_value['message'] = {}
    json_value['message']['attachment'] = {}
    json_value['message']['attachment']['type'] = 'template'
    json_value['message']['attachment']['payload'] = {}
    json_value['message']['attachment']['payload']['template_type'] = 'list'
    d = []
    for i in value['elements']:
        temp = {}
        if 'image_url' in i:
            temp['image_url'] = i['image_url']
        if 'subtitle' in i:
            temp['subtitle'] = i['subtitle']
        temp['title'] = i['title']
        temp['buttons'] = [create_for_button(i['button'])]
        d.append(temp)
    json_value['message']['attachment']['payload']['elements'] = d
    json_value['message']['attachment']['payload']['buttons'] = [create_for_button(value['button'])]
    return json_value

def create_for_button(value):
    ret = {}
    if value['type'] == 'web_url':
        ui = ['type','url','subtitle','fallback_url']
        for i in ui:
            if i in value:
                ret[i] = value[i]
    if value['type'] == 'postback':
        ui = ['type','title','payload']
        for i in ui:
            ret[i] = value[i]
    if value['type'] == 'element_share':
        ret['type'] = value['type']
    return ret