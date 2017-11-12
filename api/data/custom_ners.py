import requests

customners = [
    {
        "key": "greeting",
        "nerType": "single_match",
        "values": ["hi", "hello"]
    },
    {
        "key": "city",
        "nerType": "double_match",
        "values": ["kanpur", "hyderabad", "bangalore", "pune"]
    },
    {
        "key": "digits",
        "nerType": "regex",
        "values": ["\d+"]
    },
    {
        "key": "isFootballer",
        "nerType": "with_metadata",
        "values": [
            {
                "club": "F.C. Barcelona",
                "country": "Argentina",
                "keyword": "messi"
            },
            {
                "club": "Real Madrid",
                "country": "Portugal",
                "keyword": "ronaldo"
            },
            {
                "club": "Chelsea",
                "country": "Belgium",
                "keyword": "hazard"
            }
        ]
    },
    {
        "key": "noun_verb_adjective_barclays",
        "nerType": "database",
        "values": [
            {
                "noun": "payment",
                "verb": "understand",
                "adj": None,
                "output": "A1"
            },
            {
                "noun": "card",
                "verb": "lost",
                "adj": "credit",
                "output": "A2"
            }
        ]
    }
]

def formatCustomNers(ners):
    new_ners = {}
    databases = {}
    for ner in ners:
        if(ner['nerType'] == 'database'):
            databases[ner['key']] = ner['values']
        else:
            new_ners[ner['key']] = {'values': ner['values'], 'nerType': ner['nerType']}
    return {'new_ners': new_ners, 'databases': databases}

def getCustomNers():
    return formatCustomNers(customners)

def getCustomNersFromServer():
    # Ask Prabhjot for enterpriseId and enterpriseAccessToken
    email="bits_team2@imimobile.com"
    password="1Q&@NDq#"
    rr = requests.post("https://staging.imibot.ai/login",data={"email":email,"password":password},headers={'API-KEY':"54asdkj1209nksnda"})
    print rr.json()
    if rr.status_code == 200:
        resp = rr.json()
        auth = resp['auth_token']
        token = resp['token']
        enterpriseId = resp["_id"]
        url = 'https://staging.imibot.ai/customNer/enterprise/' + enterpriseId
        headers= {
            'x-access-token': token,"auth-token":auth
        }
        r=requests.get(url, headers=headers,verify=False)
        customners=r.json()
        # print customners8
        return formatCustomNers(customners)
