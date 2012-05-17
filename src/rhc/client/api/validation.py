import application 
import cartridge
import ssh

def validate_flag(flag, name):
    if flag and flag.lower() != "true" and flag.lower() != "false":
        raise ValueError("""%s must either be 'true' or 'false'""" % name)

def validate_exists(value, name):
    if not value or len(value) <= 0: 
        raise ValueError("""%s has no value""" % name)

def validate_is_one_of(name, thing, things):
    if not thing in things:
        raise ValueError("%s should be one of: %s"\
                % (name, str(things)))

def validate(name, expected, value):
    
    validate_exists(value, name)
    if expected == "flag": 
        validate_flag(value, name)

    elif expected == "app-action": 
        validate_is_one_of(name, expected, application.actions)

    elif expected == "app-cartridge":
        validate_is_one_of(name, expected, application.cartridges)

    elif expected == "embed-action": 
        validate_is_one_of(name, expected, cartridge.actions)

    elif expected == "embed-cartridge":
        validate_is_one_of(name, expected, cartridge.cartridges)
        
    elif expected == "key-type": 
        validate_is_one_of(name, expected, ssh.key_types)

    else:
        pass

