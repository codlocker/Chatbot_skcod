def main_function(variables):
    templateKey = ""

    if "first_time_cred" in variables["dataStore"] and variables["dataStore"]["first_time_cred"]:
        templateKey = "first_time_login"
    elif variables["newdfState"]["assignment"] and variables["newdfState"]["courses"]:
        if len(variables["newdfState"]["courses"]) > 0:
            templateKey = "courses_specified"
        else:
            templateKey = "courses_not_specified"
    else:
        templateKey = "error"

    output = {
        "templateKey": templateKey
    }
    return output

