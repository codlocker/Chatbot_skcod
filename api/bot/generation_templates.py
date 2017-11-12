def main_function(variables):
    if variables['templateKey'] == 'pushreminder':
        output = [{"include":["web"],"text": [""]}]
    elif (variables['templateKey'] == "give_time_interval"):
        output = [{"include":["web"],"text": ["Give me a valid time interval"]}]
    return output