from flask import Flask
from flask import request
from flask import jsonify
from flask import send_from_directory
from flask import Response
from flask import abort

from werkzeug import secure_filename

from setup import *


app = Flask(__name__)
#app = Flask(__name__, static_url_path='')

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
app.config['UPLOAD_FOLDER'     ] = UPLOAD_FOLDER
app.config['RNG_ID'            ] = RNG_ID
app.config['DB_NAME'           ] = DB_NAME