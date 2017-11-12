import uuid

def runCode(code, variables):
    code_globals = {'variables': variables}
    code_locals = {}
    exec code in code_globals, code_locals
    return code_locals['output']

def checkSantityAndUpdateDemandFrame(old_df, new_df):
    for key in old_df:
        if(key not in new_df):
            new_df[key] = old_df[key] # Think about whether this should be set to None or the old Value.
    return new_df

def generateUUID():
    return uuid.uuid4().urn[9:]
