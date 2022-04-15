from flask import Flask
from website import create_app

app = create_app()

from routes.dcms import *

if __name__ == '__main__':
    app.run(debug=True)
