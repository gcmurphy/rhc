import broker
import command

_path = "userinfo"
def info(**kw):
    
    url = "%s/%s" % (kw.get("broker", broker.OPENSHIFT_BROKER_URL), _path) 

    cmd = command.command({
        "debug": {"class": "optional", "type": "flag"}, 
        "password": {"class": "required", "type": "string"}, 
        "rhlogin": {"class": "required", "type": "string"}}, kw)

    return broker.broker(url, cmd)
