# INSTALL:
    sudo pip install --upgrade --requirement requirements.txt

# UUID:
    dbus-uuidgen

# ROUTES:
```
    /                                  - 404
    /UUID/                             - [GET ][JSON] List routes
    /UUID/getdb/                       - [GET ][JSON] Get db

    /UUID/data/get/<path:path>         - [GET ][JSON] Get file
    /UUID/data/del/<path:path>         - [GET ][JSON] Delete file
    /UUID/data/list/ids/               - [GET ][JSON] List all IDs
    /UUID/data/list/all/[<pi_id>]/     - [GET ][JSON] List all files
    /UUID/data/list/last/[<pi_id>]/    - [GET ][JSON] List last files
    /UUID/data/list/filepath/[<pi_id>]/- [GET ][JSON] List all file paths
    /UUID/data/list/filename/[<pi_id>]/- [GET ][JSON] List all file names
    /UUID/data/show/all/[<pi_id>]/     - [GET ][HTML] Show all data
    /UUID/data/show/last/[<pi_id>]/    - [GET ][HTML] Show last data
    /UUID/data/add/<pi_id>             - [POST:foto ][JSON] Add data from PI_ID

    /UUID/ips/list/all/[<pi_id>]/      - [GET ][JSON] Display all images
    /UUID/ips/list/last/[<pi_id>]/     - [GET ][JSON] Display last images for each PI_ID
    /UUID/ips/add/<pi_id>/[<pi_ip>]/   - [GET ][JSON] log internal [and external] IP from PI_ID

    # routes.py:     @app.route('/')
    # routes.py:     @app.route('/'+app.config['RNG_ID']+'/')
    # routes.py:     @app.route('/'+app.config['RNG_ID']+'/getdb/')

    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/get/<path:path>')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/del/<path:path>')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/all/', defaults={'pi_id': None})
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/all/<pi_id>/')
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/last/', defaults={'pi_id': None})
    # routes_data.py:@app.route('/'+app.config['RNG_ID']+'/data/list/last/<pi_id>/')
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
    # routes_ips.py: @app.route('/'+app.config['RNG_ID']+'/ips/add/<pi_id>/', defaults={'int_ip': ''})
    # routes_ips.py: @app.route('/'+app.config['RNG_ID']+'/ips/add/<pi_id>/<int_ip>/')
```

# GLOBAL
## LIST ROUTES - GET - JSON
```
curl http://pifollow-sauloal.c9.io/UUID/
```

## GET DB - GET - JSON
```
curl http://pifollow-sauloal.c9.io/UUID/getdb/
```

# DATA
## GET FILE - GET - BINARY
```
curl http://pifollow-sauloal.c9.io/UUID/data/get/<PI ID>/<FILE NAME>
```

## DELETE FILE - GET - JSON
```
curl http://pifollow-sauloal.c9.io/UUID/data/del/<PI ID>/<FILE NAME>
```

## LIST PI IDS - GET - JSON
```
curl http://pifollow-sauloal.c9.io/UUID/data/list/ids/
```

## LIST ALL FILES - GET - JSON
```
curl http://pifollow-sauloal.c9.io/UUID/data/list/all/[<PI ID>]/
```

## LIST LAST FILES - GET - JSON
```
curl http://pifollow-sauloal.c9.io/UUID/data/list/last/[<PI ID>]/
```

## LIST FILE PATHS - GET - JSON
```
curl http://pifollow-sauloal.c9.io/UUID/data/list/filepath/[<PI ID>]/
```

## LIST FILE NAMES - GET - JSON
```
curl http://pifollow-sauloal.c9.io/UUID/data/list/filename/[<PI ID>]/
```

## SHOW ALL DATA - GET - HTML
```
browser http://pifollow-sauloal.c9.io/UUID/data/show/all/[<PI ID>]/
```

## SHOW LAST DATA - GET - HTML
```
browser http://pifollow-sauloal.c9.io/UUID/data/show/last/[<PI ID>]/
```

## ADD FILE - POST - JSON
```
curl -X POST --form foto=@"FILENAME" http://pifollow-sauloal.c9.io/UUID/data/add/<PI ID>
```

# IPS
## LIST ALL IPS - GET - JSON
```
    curl http://pifollow-sauloal.c9.io/UUID/ips/list/all/[<PI ID>]/
```

## LIST LAST IPS - GET - JSON
```
    curl http://pifollow-sauloal.c9.io/UUID/ips/list/last/[<PI ID>]/
```

## ADD IP - GET - JSON
```
    curl http://pifollow-sauloal.c9.io/UUID/ips/add/<PI ID>/[<PI PRIV IP>]/
```
