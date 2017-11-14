import requests


base_url = "http://id.bits-hyderabad.ac.in/moodle/"


def get_user_token(username, password):
    api_point = "login/token.php?service=moodle_mobile_app&username={0}&password={1}".format(username, password)
    retry = 0
    cms_token = None
    while retry <= 3:
        r = requests.get(base_url + api_point, timeout=3)
        if r.status_code == 200:
            cms_token = r.json()["token"]
            # print(cms_token)
            return cms_token
        else:
            # print("Retrying...")
            retry += 1
    return cms_token


def get_user_id(cms_token):
    api_point = "webservice/rest/server.php?wsfunction=core_webservice_get_site_info&moodlewsrest" \
                + "format=json&wstoken={0}".format(cms_token)
    retry = 0
    user_id = None
    while retry <= 3:
        r = requests.get(base_url + api_point, timeout=3)
        if r.status_code == 200:
            user_id = r.json()["userid"]
            return user_id
        else:
            # print("Retrying...")
            retry += 1
    return user_id


def main_function(variables):
    df = {
        "assignment": None,
        "courses": None
    }

    data_store = {}
    if "dataStore" in variables and variables["dataStore"]:
        data_store = variables["dataStore"]
        data_store["credentials"] = False
        data_store["first_time_cred"] = False
    else:
        data_store["credentials"] = False
        data_store["first_time_cred"] = False
        variables["dataStore"] = data_store

    permanent_data_key = "consumerDataStore"
    user_message = variables["nlp"]["word_tokens"]  # nltk tokenizer used in pipelines
    if permanent_data_key in variables and variables[permanent_data_key] \
            and "cms_token" in variables[permanent_data_key] and variables[permanent_data_key]["cms_token"]:
        data_store["credentials"] = True
    elif "username" in user_message and "password" in user_message:
        '''
        User is requested to provide username and password using a strict format
        Format is:
        username: xyz password: abc
        '''
        variables[permanent_data_key] = {}
        username = variables["nlp"]["custom_ners"]["bitsid_value"][0]
        password = variables["nlp"]["actual_text"].split()[-1]
        # TODO: get the token of user using moodle API
        cms_token = get_user_token(username, password)  # function call here with username and password
        variables[permanent_data_key]["cms_token"] = cms_token

        # TODO: get userid using the cms_token from moodle API
        user_id = get_user_id(cms_token)  # function call here with token
        variables[permanent_data_key]["user_id"] = user_id

        data_store["credentials"] = True
        data_store["first_time_cred"] = True

    if data_store["credentials"] and data_store["first_time_cred"]:
        pass
    elif data_store["credentials"]:
        if "cms_assign_key" in variables["nlp"]["custom_ners"] \
            and variables["nlp"]["custom_ners"]["cms_assign_key"]:
            df["assignment"] = True
            df["courses"] = False
        elif "cms_courses_key" in variables["nlp"]["custom_ners"]:
            df["courses"] = True

    output = {"df": df, "dataStore": data_store, "consumerDataStore": variables["consumerDataStore"]}
    return output
