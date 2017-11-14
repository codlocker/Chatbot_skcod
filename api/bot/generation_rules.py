def main_function(variables):
    templateKey = ""
    messageStore = {"sendtoagent": False, "endflow": True}

    if "first_time_cred" in variables["dataStore"] and variables["dataStore"]["first_time_cred"]:
        templateKey = "first_time_login"
    elif variables["newdfState"]["assignment"]:
        templateKey = "courses_not_specified"
    elif variables["newdfState"]["courses"]:
        templateKey = "list_courses"
    else:
        templateKey = "error"

    output = {
        "templateKey": templateKey,
        "messageStore": messageStore
    }
    return output

