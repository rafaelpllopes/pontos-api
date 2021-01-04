# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'

from views import *

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    