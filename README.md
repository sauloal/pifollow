INSTALL:
sudo easy_install flask
sudo easy_install flask-sqlalchemy

ROUTES:
    '/' - 404
    '/'+RNG_ID+'/' - List routes
    '/'+RNG_ID+'/get/<path:path>' - Get file
    '/'+RNG_ID+'/getdb/' - Get db
    '/'+RNG_ID+'/show/all/' - Show all logs
    '/'+RNG_ID+'/show/last/' - Show last logs for each PI_ID
    '/'+RNG_ID+'/display/all/' - Display all images
    '/'+RNG_ID+'/display/last/' - Display last images for each PI_ID
    '/'+RNG_ID+'/log/<pi_id>/' - log external IP from PI_ID
    '/'+RNG_ID+'/log/<pi_id>/<pi_ip>/' - log both internal and external IPs from PI_ID
    '/'+RNG_ID+'/add/<pi_id>', methods=['POST'] - add data from PI_ID


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
