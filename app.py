
import json
from flask import Flask
#from website import create_app
import urllib.request, json 
from routes.dcms import *

def create_app():
    app = Flask(__name__)
    from views import views
    app.register_blueprint(views, url_prefix='/')
    return app

app = create_app()



if __name__ == '__main__':
    app.run(debug=True)




