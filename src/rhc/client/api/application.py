import broker
import command


def list(url="https://openshift.redhat.com/broker/cartlist"):
    return broker.broker(url, { "cart_type": "standalone" })

_path = "cartridge"

actions = [
    "configure", 
    "deconfigure", 
    "start", 
    "stop", 
    "restart", 
    "status"
]

# dynamic version
#cartridges = list().data.carts


# static version
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
    return _run("configure", **kw)
    
def delete(**kw):
    return _run("deconfigure", **kw)

def start(**kw):
    return _run("start", **kw)

def stop(**kw):
    return _run("stop", **kw)

def restart(**kw):
    return _run("restart", **kw)

def status(*kw): 
    return _run("status", **kw)
    
def _run(action, **kw):
    
    url = "%s/%s" % (kw.get("broker", broker.OPENSHIFT_BROKER_URL), _path) 
    kw.update({"action": action})
    cmd = command.command({
            "cartridge": { "class": "required", "type": "app-cartridge" },
            "debug": {"class": "optional", "type": "flag"}, 
            "password": {"class": "required", "type": "string"}, 
            "app_name": {"class": "required", "type": "string"}, 
            "action": {"class": "required", "type": "app-action"}, 
            "rhlogin": {"class": "required", "type": "string"
            }}, kw)

    return broker.broker(url, cmd)
