import requests

def getNLPData(pipeline, message, custom_ners):
    headers_nlp = {"content-type": "application/json"}
    # uri = "http://IntelligenceEngineStagingLB-49864761.us-west-2.elb.amazonaws.com:80/recipe"
    uri="http://hackathon-elb-108026863.us-west-2.elb.amazonaws.com/recipe"
    inputParams = {}
    # print pipeline, message, custom_ners, "checkpoint NLP"

    for library in pipeline:
        # print library, "checkpoint NLP 0"
        if(library['module'] == 'custom_ners'):
            inputParams[library['module']] = {}
            inputParams[library['module']]['custom_ners_dict'] = custom_ners
        else:
            inputParams[library['module']] = {}

    inputParams['text'] = message
    # print inputParams, "checkpoint NLP 1"
    data_nlp = {
        "pipelines": pipeline,
        "inputParams": inputParams
    }
    # print data_nlp, "checkpoing NLP 2"
    r = requests.post(uri,json=data_nlp,headers=headers_nlp)
    return r.json()
