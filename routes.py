import sys
import os
import base64

from db          import *
from funcs       import *
from routes_ips  import *
from routes_data import *



##
# ROOT
##
@app.route('/')
def hello_world():
    return abort(404)



##
# MAIN
##
@app.route('/'+app.config['RNG_ID']+'/')
def get_endpoints():
    data = {
            'endpoints':
                {
                    'GET':
                        [
                            '/',
                            '/getdb/',

                            '/data/get/<file_path>',
                            '/data/del/<file_path>',
                            '/data/list/all/[<pi_id>]/',
                            '/data/list/last/[<pi_id>]/',
                            '/data/list/filepath/[<pi_id>]/',
                            '/data/list/filename/[<pi_id>]/',
                            '/data/list/ids/',
                            '/data/show/all/[<pi_id>]/',
                            '/data/show/last/[<pi_id>]/',

                            '/ips/list/all/[<pi_id>]/',
                            '/ips/list/last/[<pi_id>]/',
                            '/ips/add/<pi_id>/',
                            '/ips/add/<pi_id>/<pi_internal_ip>/'
                        ],
                    'POST':
                        [
                            '/data/add/<pi_id>/'
                        ],
                    'error': False
                }
            }

    return jsonify(data), 200



##
# GETTERS
##
@app.route('/'+app.config['RNG_ID']+'/getdb/')
def get_db():
    if not os.path.exists(app.config['DB_NAME']):
        return abort(404)

    #content       = get_file(app.config['DB_NAME'])
    ##return Response(content, mimetype=mimetype)
    #return Response(content)

    return send_from_directory('.', app.config['DB_NAME'], as_attachment=True, attachment_filename=app.config['DB_NAME'])
