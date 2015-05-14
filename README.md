INSTALL:
    sudo easy_install flask
    sudo easy_install flask-sqlalchemy

UUID:
    dbus-uuidgen

ROUTES:
    /                                  - 404
    /UUID/                             - List routes
    /UUID/getdb/                       - Get db

    /UUID/data/get/<path:path>         - Get file
    /UUID/data/del/<path:path>         - Delete file
    /UUID/data/list/all/[<pi_id>]      - List all files
    /UUID/data/list/ids/               - List all IDs
    /UUID/data/list/filepath/[<pi_id>] - List all file paths
    /UUID/data/list/filename/[<pi_id>] - List all file names
    /UUID/data/show/all/[<pi_id>]      - Show [HTML] all data
    /UUID/data/show/last/[<pi_id>]     - Show [HTML[ last data
    /UUID/data/add/<pi_id>             - ['POST'] Add data from PI_ID

    /UUID/ips/list/all/[<pi_id>]       - Display all images
    /UUID/ips/list/last/[<pi_id>]      - Display last images for each PI_ID
    /UUID/add/<pi_id>/                 - log external IP from PI_ID
    /UUID/add/<pi_id>/<pi_ip>/         - log both internal and external IPs from PI_ID

    # routes.py:     @app.route('/')
    # routes.py:     @app.route('/'+app.config['RNG_ID']+'/')
    # routes.py:     @app.route('/'+app.config['RNG_ID']+'/getdb/')

    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/get/<path:path>')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/del/<path:path>')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/all/', defaults={'pi_id': None})
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/all/<pi_id>/')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/ids/')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/filepath/', defaults={'pi_id': None})
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/filepath/<pi_id>/')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/filename/', defaults={'pi_id': None})
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/filename/<pi_id>/')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/show/all/', defaults={'pi_id': None})
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/show/all/<pi_id>/')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/show/last/', defaults={'pi_id': None})
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/show/last/<pi_id>/')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/add/<pi_id>', methods=['POST'])

    # routes_ips.py: @app.route('/'+app.config['RNG_ID']+'/ips/list/all/', defaults={'pi_id': None})
    # routes_ips.py: @app.route('/'+app.config['RNG_ID']+'/ips/list/all/<pi_id>/')
    # routes_ips.py: @app.route('/'+app.config['RNG_ID']+'/ips/list/last/', defaults={'pi_id': None})
    # routes_ips.py: @app.route('/'+app.config['RNG_ID']+'/ips/list/last/<pi_id>/')
    # routes_ips.py: @app.route('/'+app.config['RNG_ID']+'/ips/add/<pi_id>/')
    # routes_ips.py: @app.route('/'+app.config['RNG_ID']+'/ips/add/<pi_id>/<pi_ip>/')


LIST:
    curl http://pi-sauloal.c9.io/$RND/

GET:
    curl http://pi-sauloal.c9.io/$RND/get/<FILE PATH>

GET DB:
    curl http://pi-sauloal.c9.io/$RND/getdb/

SHOW:
    curl http://pi-sauloal.c9.io/$RND/show/[ALL|LAST]/

DISPLAY:
    curl http://pi-sauloal.c9.io/$RND/display/[ALL|LAST]/

LOG:
    curl http://pi-sauloal.c9.io/$RND/log/<PI_ID>/
    curl http://pi-sauloal.c9.io/$RND/log/<PI_ID>/<PRIVATE_ID>/

ADD:
    curl -X POST --form foto=@"$FN" http://pi-sauloal.c9.io/$RND/add/<PI_ID>/
