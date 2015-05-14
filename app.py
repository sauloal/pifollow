from flask import Flask
from setup import *

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
app.config['UPLOAD_FOLDER'     ] = UPLOAD_FOLDER
