# df = {
#     "remind": None,
#     "time": None,
#     "interval": None,
#     "message": None
# }
#
# if "dataStore" in variables and variables["dataStore"] and "endflow" in variables["dataStore"] and variables["dataStore"]["endflow"]:
#     datastore = variables["dataStore"]
# else:
#     datastore = {"endflow": True}
#
# if datastore["endflow"]:
#     newdf=df
# else:
#     newdf = variables["lastdfState"]
#
# if "custom_ners" in variables["nlp"] and "remind" in variables["nlp"]["custom_ners"]:
#     newdf["remind"]=True
# if "datetime" in variables["nlp"] and variables["nlp"]["datetime"]:
#     newdf["time"]=variables["nlp"]["datetime"]["time"]
# if "numbers" in variables["nlp"] and variables["nlp"]["numbers"]:
#     newdf["interval"]=variables["nlp"]["numbers"][0]
#
#
