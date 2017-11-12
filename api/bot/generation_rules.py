def main_function(variables):
    templateKey = ""

    if variables["newdfState"]["remind"] and (variables["newdfState"]["time"] or variables["newdfState"]["interval"]):
        templateKey = "pushreminder"
        messageStore = {
            "endflow": True
        }
    else:
        templateKey = "give_time_interval"
        messageStore = {
            "endflow": True
        }

    output = {
        "templateKey": templateKey
    }
    return output

