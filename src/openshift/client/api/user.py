from openshift.client.api.broker import broker, OPENSHIFT_BROKER_URL
from openshift.client.api.command import command

_path = "userinfo"
def info(**kw):
    
    url = "%s/%s" % (kw.get("broker", OPENSHIFT_BROKER_URL), _path) 
    cmd = command({
        "debug": {"class": "optional", "type": "flag"}, 
        "password": {"class": "required", "type": "string"}, 
        "rhlogin": {"class": "required", "type": "string"}}, kw)

    return broker(url, cmd)
