RNG_ID             = 'dc97d7355965f2d9f81130ba555510e0'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
DEBUG              = True
UPLOAD_FOLDER      = 'data'
DB_NAME            = 'data.db'

images = ['png', 'jpg', 'jpeg', 'gif']

import os
if os.path.exists( 'rng.cfg' ):
    cfg = open( 'rng.cfg', 'r' ).read().strip()
    if len(cfg) > 0:
        print "using RNG '%s'" % cfg
        RNG_ID = cfg