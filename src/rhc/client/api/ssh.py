import broker
import command

_path = "ssh_keys"

key_type = [ "ssh-rsa", "ssh-dss" ]

def add(**kw):

    url = "%s/%s" % (kw.get("broker", broker.OPENSHIFT_BROKER_URL), _path) 
    cmd = command.command({
            "rhlogin": { "class": "required", "type": "string"}, 
            "ssh":  { "class" : "required", "type": "string"}, 
            "password": {"class": "required", "type": "string"}, 
            "key_type": {"class": "required", "type": "key-type"}, 
            "key_name": {"class": "required", "type": "string"}
            }, kw)

    cmd['action'] = "add-key"
    return broker(url, cmd)
   
def remove(**kw):
    
    url = "%/%s" % (kw.get("broker", broker.OPENSHIFT_BROKER_URL), _path)
    cmd = command.command({
            "rhlogin": { "class": "required", "type": "string"}, 
            "password": {"class": "required", "type": "string"}, 
            "key_type": {"class": "required", "type": "key-type"}, 
            "key_name": {"class": "required", "type": "string"}
            }, kw)

    cmd['action'] = "remove-key"
    return broker(url, cmd)

def update(**kw):

    url = "%s/%s" % (kw.get("broker", broker.OPENSHIFT_BROKER_URL), _path) 
    cmd = command.command({
            "rhlogin": { "class": "required", "type": "string"}, 
            "ssh":  { "class" : "required", "type": "string"}, 
            "password": {"class": "required", "type": "string"}, 
            "key_type": {"class": "required", "type": "key-type"}, 
            "key_name": {"class": "required", "type": "string"}
            }, kw)

    cmd['action'] = "update-key"
    return broker(url, cmd)
   
def list(**kw):

    url = "%/%s" % (kw.get("broker", broker.OPENSHIFT_BROKER_URL), _path)
    cmd = command.command({
            "rhlogin": { "class": "required", "type": "string"}, 
            "password": {"class": "required", "type": "string"}, 
            }, kw)

    cmd['action'] = "list-keys"
    return broker(url, cmd)
 
