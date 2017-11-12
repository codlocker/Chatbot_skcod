import requests
from random import randint
import requests
import json
import datetime
import calendar

df = {
    "shopping": None,
    "travel": None,
    "dining": None,
    "entertainment": None,
    "dazzleme": None,
    "ilikewhatisee": None,
    "thanks": None,
    "yesiam": None,
    "notyet": None,
    "nothanks": None,
    "iwillapplynow": None,
    "iam": None,
    "notreally": None
}

newdf = df

if variables["dataStore"]:
    datastore = variables["dataStore"]
else:
    datastore = {}

print "CUSTOM NERS"
print "CUSTOM NERS"
print "CUSTOM NERS", variables['nlp']['custom_ners']

print "NLP"
print "NLP"
print "NLP", variables['nlp']


#shopping
if "custom_ners" in variables["nlp"] and "shopping" in variables["nlp"]["custom_ners"]:
    newdf["shopping"] = variables["nlp"]["custom_ners"]["shopping_value"][0]

#travel
if "custom_ners" in variables["nlp"] and "travel" in variables["nlp"]["custom_ners"]:
    newdf["travel"] = variables["nlp"]["custom_ners"]["travel_value"][0]

#dining
if "custom_ners" in variables["nlp"] and "dining" in variables["nlp"]["custom_ners"]:
    newdf["dining"] = variables["nlp"]["custom_ners"]["dining_value"][0]

#entertainment
if "custom_ners" in variables["nlp"] and "entertainment" in variables["nlp"]["custom_ners"]:
    newdf["entertainment"] = variables["nlp"]["custom_ners"]["entertainment_value"][0]

#dazzleme
if "custom_ners" in variables["nlp"] and "dazzleme" in variables["nlp"]["custom_ners"]:
    newdf["dazzleme"] = variables["nlp"]["custom_ners"]["dazzleme_value"][0]

#ilikewhatisee
if "custom_ners" in variables["nlp"] and "ilikewhatisee" in variables["nlp"]["custom_ners"]:
    newdf["ilikewhatisee"] = variables["nlp"]["custom_ners"]["ilikewhatisee_value"][0]

#thanks
if "custom_ners" in variables["nlp"] and "thanks" in variables["nlp"]["custom_ners"]:
    newdf["thanks"] = variables["nlp"]["custom_ners"]["thanks_value"][0]

#yesiam
if "custom_ners" in variables["nlp"] and "yesiam" in variables["nlp"]["custom_ners"]:
    newdf["yesiam"] = variables["nlp"]["custom_ners"]["yesiam_value"][0]

#notyet
if "custom_ners" in variables["nlp"] and "notyet" in variables["nlp"]["custom_ners"]:
    newdf["notyet"] = variables["nlp"]["custom_ners"]["notyet_value"][0]

#nothanks
if "custom_ners" in variables["nlp"] and "nothanks" in variables["nlp"]["custom_ners"]:
    newdf["nothanks"] = variables["nlp"]["custom_ners"]["nothanks_value"][0]

#iwillapplynow
if "custom_ners" in variables["nlp"] and "iwillapplynow" in variables["nlp"]["custom_ners"]:
    newdf["iwillapplynow"] = variables["nlp"]["custom_ners"]["iwillapplynow_value"][0]

#iam
if "custom_ners" in variables["nlp"] and "iam" in variables["nlp"]["custom_ners"]:
    newdf["iam"] = variables["nlp"]["custom_ners"]["iam_value"][0]

#notreally
if "custom_ners" in variables["nlp"] and "notreally" in variables["nlp"]["custom_ners"]:
    newdf["notreally"] = variables["nlp"]["custom_ners"]["notreally_value"][0]

# if "custom_ners" in variables["nlp"] and "reset" in variables["nlp"]["custom_ners"]:
#     pass




output = {
    "df": newdf,
    "dataStore": datastore
}

