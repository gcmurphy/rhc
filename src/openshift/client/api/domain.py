from openshift.client.api.broker import broker, OPENSHIFT_BROKER_URL
from openshift.client.api.command import command

_path = "domain"
def create(**kw):
    
    url = "%s/%s" % (kw.get("broker", OPENSHIFT_BROKER_URL), _path) 
    cmd = command({
        "alter": {"class": "optional", "type": "flag"}, 
        "debug": {"class": "optional", "type": "flag"}, 
        "ssh":   {"class": "required", "type": "string"}, 
        "password": {"class": "required", "type": "string"}, 
        "namespace": {"class": "required", "type": "string"}, 
        "rhlogin": {"class": "required", "type": "string"}}, kw)

    return broker(url, cmd)
