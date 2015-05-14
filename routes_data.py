from funcs       import *
from db          import *

##
# GETTERS
##
@app.route('/'+app.config['RNG_ID']+'/data/get/<path:path>')
def get_log(path):
    complete_path = os.path.join(app.config['UPLOAD_FOLDER'], path)

    if not os.path.exists(complete_path):
        print "complete path %s does not exists" % complete_path
        return abort(404)

    if not os.path.abspath(complete_path).startswith( os.path.abspath(app.config['UPLOAD_FOLDER']) ):
        print "path %s does not starts with upload folder %s" % ( os.path.abspath(complete_path), os.path.abspath(app.config['UPLOAD_FOLDER']) )
        return abort(404)

    ##complete_path = os.path.join(root_dir(), app.config['DB_NAME'])
    ##ext           = os.path.splitext(path)[1]
    ##mimetype      = mimetypes.get(ext, "text/html")
    #content       = get_file(complete_path)
    ##return Response(content, mimetype=mimetype)
    #return Response(content)

    return send_from_directory(app.config['UPLOAD_FOLDER'], path, as_attachment=True, attachment_filename=path)


@app.route('/'+app.config['RNG_ID']+'/data/del/<path:path>')
def get_del(path):
    print 'path',path
    print 'UPLOAD_FOLDER', app.config['UPLOAD_FOLDER']
    complete_path = os.path.join(app.config['UPLOAD_FOLDER'], path)
    print 'complete_path', complete_path

    if not os.path.exists(complete_path):
        print "complete path %s does not exists" % complete_path
        return abort(404)

    if not os.path.abspath(complete_path).startswith( os.path.abspath(app.config['UPLOAD_FOLDER']) ):
        print "path %s does not starts with upload folder %s" % ( os.path.abspath(complete_path), os.path.abspath(app.config['UPLOAD_FOLDER']) )
        return abort(404)

    try:
        r = Data.query.filter_by(filepath=path).first()

        db.session.delete(r)
        db.session.commit()

        os.remove(complete_path)

        res = { 'del': path, 'error': False }

        return jsonify(res), 200

    except Exception as e:
        print "error", e
        return jsonify({ 'del': path, 'error': True, 'message': str(e) }), 501


    ##complete_path = os.path.join(root_dir(), app.config['DB_NAME'])
    ##ext           = os.path.splitext(path)[1]
    ##mimetype      = mimetypes.get(ext, "text/html")
    #content       = get_file(complete_path)
    ##return Response(content, mimetype=mimetype)
    #return Response(content)



##
# LISTS
##
@app.route('/'+app.config['RNG_ID']+'/data/list/all/', defaults={'pi_id': None})
@app.route('/'+app.config['RNG_ID']+'/data/list/all/<pi_id>/')
def list_data(pi_id):
    try:
        if pi_id is None:
            data = Data.query.all()

        else:
            data = Data.query.filter( Data.pi_id == pi_id ).all()

        data = [ x.as_dict() for x in data ]

        return jsonify({'ids': data, 'error': False}), 200

    except Exception as e:
        return jsonify({'message': str(e), 'error': True}), 200



@app.route('/'+app.config['RNG_ID']+'/data/list/ids/')
def list_data_ids():
    try:
        data = sorted( [ x.pi_id for x in db.session.query(Data.pi_id).distinct() ] )

        return jsonify({'ids': data, 'error': False}), 200

    except Exception as e:
        return jsonify({'message': str(e), 'error': True}), 200

@app.route('/'+app.config['RNG_ID']+'/data/list/filepath/', defaults={'pi_id': None})
@app.route('/'+app.config['RNG_ID']+'/data/list/filepath/<pi_id>/')
def list_data_filepath(pi_id):
    try:
        if pi_id is None:
            data = sorted( [ x.filepath for x in db.session.query(Data.filepath).distinct() ] )

        else:
            data = sorted( [ x.filepath for x in db.session.query(Data.filepath).filter(Data.pi_id == pi_id).distinct() ] )

        return jsonify({'filepath': data, 'error': False}), 200

    except Exception as e:
        return jsonify({'message': str(e), 'error': True}), 200


@app.route('/'+app.config['RNG_ID']+'/data/list/filename/', defaults={'pi_id': None})
@app.route('/'+app.config['RNG_ID']+'/data/list/filename/<pi_id>/')
def list_data_filename(pi_id):
    try:
        if pi_id is None:
            data = sorted( [ x.filename for x in db.session.query(Data.filename).distinct() ] )

        else:
            data = sorted( [ x.filename for x in db.session.query(Data.filename).filter(Data.pi_id == pi_id).distinct() ] )

        return jsonify({'filename': data, 'error': False}), 200

    except Exception as e:
        return jsonify({'message': str(e), 'error': True}), 200



##
# DISPLAY
##
@app.route('/'+app.config['RNG_ID']+'/data/show/all/', defaults={'pi_id': None})
@app.route('/'+app.config['RNG_ID']+'/data/show/all/<pi_id>/')
def display_image_all(pi_id):
    try:
        if pi_id is None:
            res = gen_table( Data.query.all(), app.config['RNG_ID'] )

        else:
            res = gen_table( Data.query.filter(Data.pi_id == pi_id).all(), app.config['RNG_ID'] )

        return res, 200

    except Exception as e:
        print "error", e
        return jsonify({ 'error': True, 'message': str(e) }), 501


@app.route('/'+app.config['RNG_ID']+'/data/show/last/', defaults={'pi_id': None})
@app.route('/'+app.config['RNG_ID']+'/data/show/last/<pi_id>/')
def display_image_last(pi_id):
    meta = """<head><meta http-equiv="refresh" content="60" /></head>"""

    try:
        if pi_id is None:
            res = gen_table( Data.query.group_by(Data.pi_id), app.config['RNG_ID'] )

        else:
            res = gen_table( Data.query.group_by(Data.pi_id).filter(Data.pi_id == pi_id), app.config['RNG_ID'] )

        return res, 200

    except Exception as e:
        print "error", e
        return jsonify({ 'error': True, 'message': str(e) }), 501



##
# ADD
##
@app.route('/'+app.config['RNG_ID']+'/data/add/<pi_id>', methods=['POST'])
def add(pi_id):
    file     = request.files['foto']
    filename = file.filename
    filesize = request.content_length

    path = os.path.join(app.config['UPLOAD_FOLDER'], pi_id                    )
    dst  = os.path.join(pi_id                      , secure_filename(filename))
    dstn = os.path.join(app.config['UPLOAD_FOLDER'], dst                      )

    if not os.path.exists(path):
        os.makedirs(path)

    file.save(dstn)

    print "ADDING ID %s NAME %s SIZE %d PATH %s" % (pi_id, filename, filesize, dst)
    info     = Data(pi_id, filename, filesize, dst)

    db.session.add(info)

    try:
        db.session.commit()

        return jsonify({'pi_id': pi_id, 'filename': filename, 'filesize': filesize, 'error': False}), 200

    except:
        return jsonify({'pi_id': pi_id, 'filename': filename, 'filesize': filesize, 'error': True, 'message': 'record exists'}), 501

