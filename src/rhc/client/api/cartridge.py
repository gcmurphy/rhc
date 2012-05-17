import broker
import command

_cartlist_url="%s/%s" % (broker.OPENSHIFT_BROKER_URL), "cartlist")

def list(url=_cartlist_url):
    return broker(url, { "cart_type": "embedded" })

_path = "embed_cartridge"

actions = [
    "configure", 
    "deconfigure"
]

# dynamic version
cartridges = list().data.carts

"""
# static version
cartridges = [ 
    "mongodb-2.0", 
    "cron-1.4", 
    "mysql-5.1", 
    "postgresql-8.4", 
    "haproxy-1.4", 
    "10gen-mms-agent-0.1", 
    "phpmyadmin-3.4",
    "metrics-0.1", 
    "rockmongo-1.1", 
    "jenkins-client-1.4"
]
"""

def configure(**kw):
    return _run("configure", **kw)
    
def deconfigure(**kw):
    return _run("deconfigure", **kw)

def _run(action, **kw):
    
    url = "%s/%s" % (kw.get("broker", broker.OPENSHIFT_BROKER_URL), _path) 
    kw.update({"action": action})
    cmd = command.command({
            "cartridge": { "class": "required", "type": "embed-cartridge" },
            "debug": {"class": "optional", "type": "flag"}, 
            "password": {"class": "required", "type": "string"}, 
            "app_name": {"class": "required", "type": "string"}, 
            "action": {"class": "required", "type": "embed-action"}, 
            "rhlogin": {"class": "required", "type": "string"
            }}, kw)

    return broker.broker(url, cmd)
