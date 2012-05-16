from openshift.client.api.broker import broker, OPENSHIFT_BROKER_URL
from openshift.client.api.command import command

_path = "cartridge"

actions = [
    "configure", 
    "deconfigure", 
    "start", 
    "stop", 
    "restart", 
    "status"
]

cartridges = [ 
    "nodejs-0.6", 
    "jbossas-7", 
    "python-2.6", 
    "jenkins-1.4",
    "ruby-1.8", 
    "diy-0.1", 
    "php-5.3", 
    "perl-5.10"
]

def create(**kw):
    _run("configure", **kw)
    
def delete(**kw):
    _run("deconfigure", **kw)

def start(**kw):
    _run("start", **kw)

def stop(**kw):
    _run("stop", **kw)

def restart(**kw):
    _run("restart", **kw)

def status(*kw): 
    _run("status", **kw)
    
def _run(action, **kw):
    
    url = "%s/%s" % (kw.get("broker", OPENSHIFT_BROKER_URL), _path) 
    kw.update({"action": action})
    cmd = command({
            "cartridge": { "class": "required", "type": "app-cartridge" },
            "debug": {"class": "optional", "type": "flag"}, 
            "password": {"class": "required", "type": "string"}, 
            "app_name": {"class": "required", "type": "string"}, 
            "action": {"class": "required", "type": "app-action"}, 
            "rhlogin": {"class": "required", "type": "string"
            }}, kw)

    return broker(url, cmd)
