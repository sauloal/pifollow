import sys
import os
import base64

from flask import request
from flask import jsonify
from flask import Response
from werkzeug import secure_filename

from db    import *
from funcs import *


@app.route('/')
def hello_world():
    return 404

##
# ROOT
##
@app.route('/'+RNG_ID+'/')
def endpoints():
    data = {
            'endpoints':
                { 
                    'GET': 
                        ['/get/<file_path>', '/getdb/', '/show/all', '/show/last', '/display/all/', '/display/last/', '/log/<pi_id>/', '/log/<pi_id>/<pi_internal_ip>/'], 
                    'POST': 
                        ['/add/<pi_id>[POST]'], 
                    'error': False 
                }
            }
    return jsonify(data), 200

@app.route('/'+RNG_ID+'/get/<path:path>')
def get_log(path):
    complete_path = path
    if not os.path.exists(complete_path):
        return 404
        
    if not complete_path.startswith(app.config['UPLOAD_FOLDER']):
        return 404
        
    #complete_path = os.path.join(root_dir(), db_name)
    #ext           = os.path.splitext(path)[1]
    #mimetype      = mimetypes.get(ext, "text/html")
    content       = get_file(complete_path)
    #return Response(content, mimetype=mimetype)
    return Response(content)


@app.route('/'+RNG_ID+'/getdb/')
def get_db():
    if not os.path.exists(DB_NAME):
        return 404

    content       = get_file(DB_NAME)
    #return Response(content, mimetype=mimetype)
    return Response(content)

    

##
# SHOW
##
@app.route('/'+RNG_ID+'/show/all/')
def show_log_all():
    try:
        res = { 'all': [ x.as_dict() for x in Ips.query.all()], 'error': False }
        return jsonify(res), 200
    except Exception as e:
        print "error", e
        return jsonify({ 'error': True, 'message': str(e) }), 200

@app.route('/'+RNG_ID+'/show/last/')
def show_log_last():
    try:
        res = { 'last': [ x.as_dict() for x in Ips.query.group_by(Ips.pi_id) ], 'error': False }
        return jsonify(res), 200
    except Exception as e:
        print "error", e
        return jsonify({ 'error': True, 'message': str(e) }), 200
    

##
# DISPLAY
##
@app.route('/'+RNG_ID+'/display/all/')
def display_image_all():
    try:
        res = """
<html>
<body>
<table>
"""
        for info in Data.query.all():
            res += """
<tr><td><h5>%(id)s</h5></td></tr>
<tr><td>%(fn)s</td></tr>
<tr><td><small>%(fs)d bytes - %(tm)s</small></td></tr>
<tr><td><img src="/%(rg)s/get/%(fp)s"/></tr></td>""" % { 'id':info.pi_id,'fn':info.filename,'fs':info.filesize,'tm':info.when,'fp':info.filepath,'rg':RNG_ID }


#<tr><td><img src="data:image/png;base64,""" % ( info.pi_id, info.filename, info.filesize, info.when )
#            res += base64.b64encode(info.file)
#            res += """"/></tr></td>
#"""

        res += """
</table>
</body>
</html>
        """
        return res, 200
    except Exception as e:
        print "error", e
        return jsonify({ 'error': True, 'message': str(e) }), 200


@app.route('/'+RNG_ID+'/display/last/')
def display_image_last():
    try:
        res = """
<html>
<head><meta http-equiv="refresh" content="60" /></head>
<body>
<table>
"""
        for info in Data.query.group_by(Data.pi_id):
            res += """
<tr><td><h2>%(id)s</h2></td></tr>
<tr><td><h3>%(fn)s</h3></td></tr>
<tr><td><small>%(fs)d bytes - %(tm)s</small></td></tr>
<tr><td><img src="/%(rg)s/get/%(fp)s"/></tr></td>""" % { 'id':info.pi_id,'fn':info.filename,'fs':info.filesize,'tm':info.when,'fp':info.filepath,'rg':RNG_ID }


#<tr><td><img src="data:image/png;base64,""" % ( info.pi_id, info.filename, info.filesize, info.when )
#            res += base64.b64encode(info.file)
#            res += """"/></tr></td>
#"""


        res += """
</table>
</body>
</html>
        """
        return res, 200
    except Exception as e:
        print "error", e
        return jsonify({ 'error': True, 'message': str(e) }), 200
    

##
# LOG
##
@app.route('/'+RNG_ID+'/log/<pi_id>/')
def log(pi_id):
    
    info = Ips(pi_id, request.remote_addr, '')
    
    db.session.add(info)
    db.session.commit()
    
    return jsonify({'pi_id': pi_id, 'ip': request.remote_addr, 'error': False}), 200

    
@app.route('/'+RNG_ID+'/log/<pi_id>/<pi_ip>/')
def log_ip(pi_id, pi_ip):
    
    info = Ips(pi_id, request.remote_addr, pi_ip)
    
    db.session.add(info)
    db.session.commit()
    
    return jsonify({'pi_id': pi_id, 'external_ip': request.remote_addr, 'internal_ip': pi_ip, 'error': False}), 200


##
# ADD
##
@app.route('/'+RNG_ID+'/add/<pi_id>', methods=['POST'])
def add(pi_id):
    file     = request.files['foto']
    filename = file.filename
    filesize = request.content_length

    path = os.path.join(app.config['UPLOAD_FOLDER'], pi_id)
    dst  = os.path.join(path, secure_filename(filename))
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    file.save(dst)
    
    info     = Data(pi_id, filename, filesize, dst)
    
    db.session.add(info)
    db.session.commit()

    return jsonify({'pi_id': pi_id, 'filename': filename, 'filesize': filesize, 'error': False}), 200
