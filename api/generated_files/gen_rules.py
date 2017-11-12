def main_function(variables):
    templateKey = ""
    messageStore = {}


    if 'reset' in variables['nlp']['custom_ners'] and variables['nlp']['custom_ners']['reset']:
        templateKey = "what_can_you_do"
        messageStore = {
            "endflow": False,
            "sendtoagent": False
         }


    if "nlp" in variables and "commonsense" in variables["nlp"] and variables["nlp"]["commonsense"] and variables["nlp"]["commonsense"]["tag"] == "isGreeting":
        templateKey = "greetingmessage"

    if "dazzleme" in variables["nlp"]["custom_ners"]:
        templateKey = "deals"
        if "shopping" in variables["nlp"]["custom_ners"]:
            #present webview for the selected list
            templateKey = "shopping"
            if "amazonapp" in variables["nlp"]["custom_ners"]:
                templateKey = "amazonapp"
        elif "travel" in  variables["nlp"]["custom_ners"]:
            #present webview for the selected list
            templateKey = "travel"
        elif "dining" in variables["nlp"]["custom_ners"]:
            #present webview for the selected list
            templateKey = "dining"
        elif "entertainment" in variables["nlp"]["custom_ners"]:
            #present webview for the selected list
            templateKey = "entertainment"
            if "ilikewhatisee" in variables["nlp"]["custom_ners"]:
                 templateKey = "ilikewhatisee"
                 if "yesiam" in variables["nlp"]["custom_ners"]:
                     templateKey = "yesiam"
                     if "iam" in variables["nlp"]["custom_ners"]:
                         templateKey = "iam"
                     elif "notreally" in variables["nlp"]["custom_ners"]:
                         templateKey = "notreally"
                 elif "notyet" in variables["nlp"]["custom_ners"]:
                     templateKey = "notyet"
                     if "nothanks" in variables["nlp"]["custom_ners"]:
                         templateKey = "nothanks"
                     elif "iwillapplynow" in variables["nlp"]["custom_ners"]:
                         templateKey = "iwillapplynow"
            elif "thanks" in variables["nlp"]["custom_ners"]:
                templateKey = "isThanks"








    # if "commonsense" in variables["nlp"] and variables["nlp"]["commonsense"]:
    #     templateKey = "commonsense"
    output = {
        "templateKey": templateKey,
        "messageStore": messageStore,
    }
    return output



# k = {"aaa":"bbb"}
# {"nlp":{"customners":{}}}