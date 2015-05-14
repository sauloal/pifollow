from funcs       import *
from db          import *

##
# SHOW
##
@app.route('/'+app.config['RNG_ID']+'/ips/list/all/', defaults={'pi_id': None})
@app.route('/'+app.config['RNG_ID']+'/ips/list/all/<pi_id>/')
def show_log_all(pi_id):
    try:
        if pi_id is None:
            res = { 'all': [ x.as_dict() for x in Ips.query.all() ], 'error': False }

        else:
            res = { 'all': [ x.as_dict() for x in Ips.query.filter(Ips.pi_id == pi_id).all() ], 'error': False }

        return jsonify(res), 200

    except Exception as e:
        print "error", e
        return jsonify({ 'error': True, 'message': str(e) }), 200


@app.route('/'+app.config['RNG_ID']+'/ips/list/last/', defaults={'pi_id': None})
@app.route('/'+app.config['RNG_ID']+'/ips/list/last/<pi_id>/')
def show_log_last(pi_id):
    try:
        if pi_id is None:
            res = { 'last': [ x.as_dict() for x in Ips.query.group_by(Ips.pi_id) ], 'error': False }

        else:
            res = { 'last': [ x.as_dict() for x in Ips.query.group_by(Ips.pi_id).filter(Ips.pi_id == pi_id) ], 'error': False }

        return jsonify(res), 200

    except Exception as e:
        print "error", e
        return jsonify({ 'error': True, 'message': str(e) }), 501


##
# LOG
##
@app.route('/'+app.config['RNG_ID']+'/ips/add/<pi_id>/')
def log(pi_id):

    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
        #print " fwd      ", request.headers.getlist("X-Forwarded-For")
        #print " forwarded", ip
        #print " request  ", ip

    else:
        ip = request.remote_addr
        print " request  ", ip

    #print request.access_route

    info = Ips(pi_id, request.remote_addr, '')

    db.session.add(info)
    db.session.commit()

    return jsonify({'pi_id': pi_id, 'ip': request.remote_addr, 'error': False}), 200


@app.route('/'+app.config['RNG_ID']+'/ips/add/<pi_id>/<pi_ip>/')
def log_ip(pi_id, pi_ip):

    info = Ips(pi_id, request.remote_addr, pi_ip)

    db.session.add(info)
    db.session.commit()

    return jsonify({'pi_id': pi_id, 'external_ip': request.remote_addr, 'internal_ip': pi_ip, 'error': False}), 200



