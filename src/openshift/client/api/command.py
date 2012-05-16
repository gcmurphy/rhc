
import validation

def command(specs, args):

    cmd = dict()
    for key in specs: 
    
        mandatory = specs[key]['class'] == "required"
        if mandatory and not args.has_key(key): 
            raise ValueError("%s is a required field" % key)

        if args.has_key(key):
            value = args.get(key)
            validation.validate(key, specs[key]['type'], value)
            cmd[key] = value
        
    return cmd
