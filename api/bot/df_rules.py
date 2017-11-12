def main_function(variables):
    df = {
        "assignment": None,
        "course": None
    }

    data_store = None
    if "dataStore" in variables and variables["dataStore"]:
        data_store = variables["dataStore"]
        data_store["credentials"] = False
    else:
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
        username = variables["nlp"]["custom_ners"]["bitsid"]
        password = user_message[-1]
        # TODO: get the token of user using moodle API
        cms_token = "" # function call here with username and password
        variables[permanent_data_key]["cms_token"] = cms_token

        # TODO: get userid using the cms_token from moodle API
        user_id = "" # function call here with token
        variables[permanent_data_key]["user_id"] = user_id

        data_store["credentials"] = True

    if data_store["credentials"]:
        pass

    output = {"df": df, "dataStore": data_store}
    return output
