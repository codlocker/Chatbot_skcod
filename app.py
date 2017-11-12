from api import app
from api import routes
app.run(host='0.0.0.0',port=5000,debug=True, threaded=False)
