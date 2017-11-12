import os
from flask import Flask
app = Flask(__name__, static_url_path='')

FILE_PATH = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
APP_PATH = os.path.split(FILE_PATH)[0] #i.e. /path/to/dir/

# import requests
# requests.post("http://internal-int-staging-2003543582.us-west-2.elb.amazonaws.com/scheduler",json={"url":"https://staging.imibot.ai/webhook","time":25,"data":{"entry":[{"messaging":[{"message":{"text":"hi"},"sender":{"id":variables["consumerData"]["facebookId"]},"recipient":{"id":"pageid"}}]}]}})

# import requests
# requests.post("http://internal-int-staging-2003543582.us-west-2.elb.amazonaws.com/scheduler",json={"url":"https://staging.imibot.ai/webhook","time":25,"data":{"entry":[{"messaging":[{"message":{"text":"hi"},"sender":{"id":100002205811895},"recipient":{"id":1354878537927602}}]}]}})

# req = requests.post("https://staging.imibot.ai/webhook",json={"entry":[{"messaging":[{"message":{"text":"hi"},"sender":{"id":"100002205811895"},"recipient":{"id":"1354878537927602"}}]}]})
#
# print req.json()
