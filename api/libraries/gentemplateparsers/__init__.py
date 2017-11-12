max_list = 'max_list'
min_list = 'min_list'
typee = 'typee'
dict = 'dict'
list = 'list'
values = 'values'
req = 'req'
notreq = 'notreq'
string = 'string'
payload ='payload'
max = 'max'
min = 'min'
objects_list = 'objects'
title = 'title'
sub_title = 'sub_title'
number = 'number'
floats = 'floats'
boolean = 'boolean'
validators = 'validators'


types = {'list':[],'string':'','number':1,'dict':{},'floats':1.2,'boolean':True}

# text = {typee:list,min_list:1,objects_list:{typee:string}}
# audio = {typee:list,objects_list:{typee:dict,req:{'url':{typee:string}}}}
# video = {typee:list,objects_list:{typee:dict,req:{'url':{typee:string}}}}
# image = {typee:list,objects_list:{typee:dict,req:{'url':{typee:string}}}}
# file = {typee:list,objects_list:{typee:dict,req:{'url':{typee:string}}}}
text = {typee:string}
audio = {typee:dict,req:{'url':{typee:string}}}
video = {typee:dict,req:{'url':{typee:string}}}
image = {typee:dict,req:{'url':{typee:string}}}
file = {typee:dict,req:{'url':{typee:string}}}
data_mappings_global = {'text':text,'audio':audio,'video':video,'image':image,'file':file}
