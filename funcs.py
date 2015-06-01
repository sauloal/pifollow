#http://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
import os
import datetime

from setup import *

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()

    except IOError as exc:
        return str(exc)

GIGA_BYTE = 1024 * 1024 * 1024.0
MEGA_BYTE = 1024 * 1024.0
KILO_BYTE = 1024.0
def conv_size(size):
    if   size >= GIGA_BYTE:
        return "{:5.1f} Gb".format(size / GIGA_BYTE)
    elif size >= MEGA_BYTE:
        return "{:5.1f} Mb".format(size / MEGA_BYTE)
    elif size >= KILO_BYTE:
        return "{:5.1f} Kb".format(size / KILO_BYTE)
    else:
        return "{:d} b".format(size)

def gen_table(qry, RNG_ID, meta=""):
    try:
        res = """
<html>
%s
<body>
<table>
""" % meta

        for info in qry:
            data   = { 'id':info.pi_id,'fn':info.filename,'fs':info.filesize,'fsc':conv_size(info.filesize),'tm':info.when,'fp':info.filepath,'rg':RNG_ID }

            if any([info.filename.lower().endswith(x) for x in images]):
                field  = """<tr><td><img src="/%(rg)s/data/get/%(fp)s"/></tr></td>""" % data

            else:
                field  = """<tr><td><a href="/%(rg)s/data/get/%(fp)s">%(fp)s</a></tr></td>""" % data

            res   += """
<tr><td><strong>%(id)s</strong> :: %(fn)s :: <small>%(tm)s - %(fsc)s</small></td></tr>
""" % data + field

        res += """
</table>
</body>
</html>
        """

        return res

    except:
        raise


def is_too_late(min_time=8, max_time=19, dst=2):
    curr = datetime.datetime.time(datetime.datetime.now())

    #print "curr"  , curr
    #print "tzname", curr.tzname()
    #print "dst"   , curr.dst()

    hour = curr.hour

    #print "hour"  , hour

    hour += dst # CET time

    if hour >= 24:
        hour -= 24

    is_less_than_min =  hour < min_time
    is_more_than_max =  hour > max_time
    is_late          = (is_less_than_min or is_more_than_max)

    #print "hour %d <%d=%s >%d=%s is late: %s" % (hour, min_time, is_less_than_min, max_time, is_more_than_max, is_late)

    if is_late:
        return True

    else:
        return False
