import random
def text_parser(value,id):
    return value[id]

def web_parser_final(web_entries):
    size = 0
    for entry in web_entries:
        for key in entry:
            size = len(entry[key])
            break
    ra = random.randint(0, size-1)
    for entry in web_entries:
        for key in entry:
            return entry[key][ra]