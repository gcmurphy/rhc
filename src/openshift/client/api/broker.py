
from bunch import bunchify
import simplejson as json 
import requests
import validation

OPENSHIFT_BROKER_URL = "https://openshift.redhat.com/broker"

def broker(url, cmd):
    
    postdata = {}
    if cmd['password']: 
        postdata['password'] = cmd['password']
        del cmd['password']

    postdata['json_data'] = json.dumps(cmd)
    rsp = requests.post(url, data=postdata)
    
    # Allow 400 status code as will most likely get message 
    # back from OpenShift API that will make more sense than 
    # a HTTP error

    if rsp.status_code != 200 and rsp.status_code != 400:
        rsp.raise_for_status()

    d = json.loads(rsp.text)
    if d.has_key('data') and len(d['data']) > 0: 
        data = json.loads(d['data'])
        d['data'] = data
    
    rv = bunchify(d)
    if int(rv.exit_code) != 0: 
        raise RuntimeError("ERROR <%(exit_code)d>: %(result)s.\n%(debug)s" % rv)

    return rv 
