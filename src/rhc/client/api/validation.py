
import application 

def validate_flag(flag, name):
    if flag and flag.lower() != "true" and flag.lower() != "false":
        raise ValueError("""%s must either be 'true' or 'false'""" % name)

def validate_exists(value, name):
    if not value or len(value) <= 0: 
        raise ValueError("""%s has no value""" % name)

def validate(name, expected, value):
    
    validate_exists(value, name)
    if expected == "flag": 
        validate_flag(value, name)

    elif expected == "app-action": 
        if not value in application.actions:
            raise ValueError("%s should be one of: %s"\
                % (name, str(application.actions)))

    elif expected == "app-cartridge":
        if not value in application.cartridges:
            raise ValueError("%s should be one of: %s"\
                % (name, str(application.cartridges)))
        
    else:
        pass

